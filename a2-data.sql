-- Data prepapred by Davood Rafiei, drafiei@ualberta.ca
-- Data prepared by Aaron Lin, ayl@ualberta.ca, and published on Sept 27, 2022
-- Data revised by Aaron Lin, ayl@ualberta.ca, and published on Sept 30, 2022
-- (Initial set of data was provided by Davood Rafiei, drafiei@ualberta.ca, then expanded by
-- Aaron Lin)

PRAGMA foreign_keys = ON;

insert into users values ('u10','Davood Rafiei');
insert into users values ('u20','Hamed Mirzaei');
insert into users values ('u30','Richard');
insert into users values ('u40','Nicole');

insert into songs values (5, 'Wavin flag', 220);
insert into songs values (10, 'Nice for what', 210);
insert into songs values (11, 'Hold on, we are going home', 227);
insert into songs values (12, 'The Database Song', 227);
insert into songs values (13, 'Jacks 291 Adventure', 230);
insert into songs values (14, 'The Campfire Song Song', 73);
insert into songs values (15, 'Never Gonna Give You Up', 215);
insert into songs values (16, 'My Heart Will Go On', 280);
insert into songs values (17, 'When Youre Gone', 205);
insert into songs values (18, 'Take Me to Your Heart', 240);
insert into songs values (19, 'My Favorite Song', 5);

insert into sessions values ('u10', 1, '2022-09-27', '2022-09-28');
insert into sessions values ('u10', 2, '2022-10-27', '2023-09-28');
insert into sessions values ('u20', 1, '2021-09-01', '2022-09-27');
insert into sessions values ('u30', 1, '2022-09-25', '2022-09-27');
insert into sessions values ('u40', 1, '2022-08-25', '2022-09-27');

insert into listen values ('u10', 1, 12, 3.5);
insert into listen values ('u10', 1, 13, 5.0);
insert into listen values ('u10', 1, 15, 10.0);
insert into listen values ('u10', 1, 16, 3.0);
insert into listen values ('u10', 2, 11, 2.0);
insert into listen values ('u10', 2, 5, 1.2);
insert into listen values ('u10', 2, 10, 1.2);
insert into listen values ('u20', 1, 5, 1.2);
insert into listen values ('u20', 1, 13, 2.0);
insert into listen values ('u20', 1, 14, 5.0);
insert into listen values ('u20', 1, 15, 1000.0);
insert into listen values ('u20', 1, 16, 3.0);
insert into listen values ('u30', 1, 5, 2.0);
insert into listen values ('u30', 1, 14, 1.0);
insert into listen values ('u30', 1, 15, 2.0);
insert into listen values ('u40', 1, 5, 2.0);
insert into listen values ('u40', 1, 10, 3.0);
insert into listen values ('u40', 1, 11, 4.0);
insert into listen values ('u40', 1, 12, 5.0);
insert into listen values ('u40', 1, 13, 6.0);
insert into listen values ('u40', 1, 14, 7.0);
insert into listen values ('u40', 1, 15, 28.0);
insert into listen values ('u40', 1, 16, 9.0);
insert into listen values ('u40', 1, 17, 10.0);
insert into listen values ('u40', 1, 18, 11.0);

insert into playlists values (30, 'Songs for 291', 'u10');
insert into playlists values (40, 'Almost all of the songs in existence', 'u40');
insert into playlists values (50, 'RIIIICCCCCCKKKKK', 'u40');
insert into playlists values (60, 'My favorite songs', 'u30');
insert into playlists values (70, 'Other songs for 291', 'u10');

insert into plinclude values (30, 10, 1);
insert into plinclude values (30, 11, 2);
insert into plinclude values (30, 5, 3);
insert into plinclude values (40, 5, 1);
insert into plinclude values (40, 10, 2);
insert into plinclude values (40, 11, 3);
insert into plinclude values (40, 12, 4);
insert into plinclude values (40, 13, 5);
insert into plinclude values (40, 14, 6);
insert into plinclude values (40, 15, 7);
insert into plinclude values (50, 15, 1);
insert into plinclude values (50, 18, 2);
insert into plinclude values (70, 5, 1);
insert into plinclude values (70, 10, 2);
insert into plinclude values (70, 11, 3);
insert into plinclude values (70, 12, 4);
insert into plinclude values (70, 13, 5);
insert into plinclude values (70, 18, 6);

insert into artists values ('a10', 'Drake', 'Canada');
insert into artists values ('a20', 'Bob Ezrin', 'Canadian');
insert into artists values ('a30', 'John', 'canada');
insert into artists values ('a40', 'Jack', 'canadian');
insert into artists values ('a50', 'SpongeBob SquarePants', 'CANADIAN');
insert into artists values ('a60', 'Rick Astley', 'british');
insert into artists values ('a70', 'Celine Dion', 'CanaDian');
insert into artists values ('a80', 'Avril Lavigne', 'cANAda');

insert into perform values ('a10', 5);
insert into perform values ('a20', 10);
insert into perform values ('a20', 11);
insert into perform values ('a30', 12);
insert into perform values ('a30', 19);
insert into perform values ('a40', 13);
insert into perform values ('a50', 14);
insert into perform values ('a60', 15);
insert into perform values ('a60', 18);
insert into perform values ('a70', 16);
insert into perform values ('a80', 17);