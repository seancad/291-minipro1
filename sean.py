from operator import indexOf
import sqlite3


db = sqlite3.connect("database.db")
conn = db.cursor()

'''
with open('a2-tables.sql', 'r') as sql_table_file:
    sql_script = sql_table_file.read()
conn.executescript(sql_script)
with open('a2-data.sql', 'r') as sql_data_file:
    sql_script = sql_data_file.read()
conn.executescript(sql_script)
'''




# returns unique keyword list


def keyword_parser(inp_str):
    keywords = []
    temp = inp_str.split(" ")

    for i in temp:
        print(i.isalnum())
        if i not in keywords and i != "":
            keywords.append(i.lower())
    return keywords

def search_for_songs_and_playlists():
    def search_menu_printer(lst, index):
        print(lst)
        size = len(lst[index:])
        printed_list = []
        for i in range(size) if (size < 5) else range(5):
            datatype = lst[index][1]['datatype']
            print('['+str(index+1)+']', "| ", "id:", lst[index][1]['content'][0],
                "| title:", lst[index][1]['content'][1],
                "| duration:", lst[index][1]['content'][2],
                "| type:", lst[index][1]['datatype'])
            printed_list.append(index)
            index += 1
        return index, printed_list

    usr_inp = input("Keywords to lookup? (seperated by spaces) ")
    keywords = keyword_parser(usr_inp)
    print(keywords)
    song_dictionary = {}
    for keyword in keywords:
        conn.execute("select sid as id, title, duration from songs where lower(title) LIKE ?",
                    ('%'+keyword.lower()+'%',))
        for row in conn.fetchall():
            sid = row[0]
            title = row[1]
            count = title.lower().count(keyword)
            if sid in song_dictionary:
                song_dictionary[sid]['count'] += count
            else:
                song_dictionary[sid] = {'content': row,
                                        'count': count, 'datatype': "song"}
    artists_dictionary = {}
    for keyword in keywords:
        conn.execute("SELECT p.pid, p.title,sum(s.duration) from playlists p\
            join plinclude pl on pl.pid = p.pid join songs s  on pl.sid = s.sid group by p.pid having lower(p.title) LIKE ?",
                    ('%'+keyword.lower()+'%',))
        for row in conn.fetchall():
            pid = row[0]
            title = row[1]
            count = title.lower().count(keyword)
            if pid in artists_dictionary:
                artists_dictionary[pid]['count'] += count
            else:
                artists_dictionary[pid] = {'content': row,
                                        'count': count, 'datatype': "playlist"}

    combined_list = list(artists_dictionary.items()) + \
        list(song_dictionary.items())
    print(artists_dictionary)
    sorted_output = sorted(combined_list,
                        key=lambda x: x[1]['count'], reverse=True)
    index = 0
    print(sorted_output)
    size = len(sorted_output)
    index, printed_list = search_menu_printer(sorted_output, index)

    while (True):
        usr_inp = input(
            "Type C to list 5 more results\nType number to select option\nType W to return:\n")
        print(printed_list)
        if (usr_inp.lower() == "c"):
            remain = len(sorted_output[index:])
            if (remain <= 0):
                print("NO RESULTS LEFT")
                continue
            index, printed_list = search_menu_printer(sorted_output, index)
        elif (usr_inp.isdigit()):
            usr_inp = int(usr_inp) - 1
            if usr_inp in printed_list:
                if (sorted_output[usr_inp][1]['datatype'] == "playlist"):
                    print("Printing all songs in playlist:\n",
                    sorted_output[usr_inp][1]['datatype'])
                    conn.execute("SELECT s.sid, s.title, s.duration from playlists p\
                        join plinclude pl on pl.pid = p.pid join songs s  on pl.sid = s.sid \
                            where p.pid = ?", [sorted_output[usr_inp][0], ])
                    for row in conn.fetchall():
                        print("id:", row[0],
                            "| title:", row[1],
                            "| duration:", row[2])
                if (sorted_output[usr_inp][1]['datatype'] == "song"):
                    print("song action")
        elif (usr_inp.lower() == "w"):
            break

def search_artists_and_songs():     
    usr_inp = input("Keywords to lookup? (seperated by spaces) ")
    keywords = keyword_parser(usr_inp)
    print(keywords)
    artists_dictionary = {}
    song_dictionary = {}
    for keyword in keywords:
        conn.execute("SELECT a.aid,a.name,a.nationality,s.title,s.sid,s.duration from artists a \
            join perform p on p.aid = a.aid join songs s on s.sid = p.sid where lower(s.title) LIKE ? or a.name like ? ",
                    ('%'+keyword.lower()+'%','%'+keyword.lower()+'%'))
        for row in conn.fetchall():
            print(row)
            aid = row[0]
            name= row[1]
            title = row[3]
            
            count = title.lower().count(keyword)
            print(count, row)
            if aid in song_dictionary:
                song_dictionary[aid]['count'] += count
                if title not in song_dictionary[aid]['songs']:
                    song_dictionary[aid]['songs'][title] = {'id':row[4],'title':title,'duration':row[5]}
            else:
                starting_count = 0
                for k in keywords:
                    starting_count += name.lower().count(k)
                count += starting_count
                print(count,"first time",starting_count)
                song_dictionary[aid] = {'name':name,'nationality':row[2],'songs' : {title:{'id':row[4],'title':title,'duration':row[5]}},
                                        'count': count}
            print("sonic",song_dictionary[aid])
    sorted_output = sorted(list(song_dictionary.items()),
                            key=lambda x: x[1]['count'], reverse=True)


    def search_menu_printer(lst, index):
            size = len(lst[index:])
            printed_list = []
            for i in range(size) if (size < 5) else range(5):

                print('['+str(index+1)+']', "| ", "name:", lst[index][1]['name'],
                    "| nationality:", lst[index][1]['nationality'],
                    "| total songs:", len(lst[index][1]['songs'].keys())) 
                printed_list.append(index)
                index += 1
            return index, printed_list                        
    index = 0
    size = len(sorted_output)

    index, printed_list = search_menu_printer(sorted_output, index)
    while (True):
            usr_inp = input(
                "Type C to list 5 more results\nType number to select option\nType W to return:\n")
            print(printed_list)
            if (usr_inp.lower() == "c"):
                remain = len(sorted_output[index:])
                if (remain <= 0):
                    print("NO RESULTS LEFT")
                    continue
                index, printed_list = search_menu_printer(sorted_output, index)
            elif (usr_inp.isdigit()):
                usr_inp = int(usr_inp) - 1
                if usr_inp in printed_list:
                    songs = sorted_output[usr_inp][1]['songs'] 
                    num_songs = len(songs.keys())
                    for i,key in enumerate(songs.keys()):      
                        song = sorted_output[usr_inp][1]['songs'][key]
                        print('['+str(i+1)+']', "| id: ",song['id'],"| title: ",
                            song['title'],"| duration: ",song['duration'])
                    usr_inp = input("TType a song index to choose it: ")
                    if usr_inp.isdigit():
                        usr_inp = int(usr_inp) - 1
                        if usr_inp in range(num_songs):
                            print('song action')
                
            elif (usr_inp.lower() == "w"):
                break