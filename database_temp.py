import sqlite3
#########
def initial_temp_data():
    conn = sqlite3.connect("nba_stats.db")  #创建sqlite.db数据库
    print ("open database success")
    conn.execute("drop table IF EXISTS temp_data")
    query = """create table IF NOT EXISTS temp_data(
        A VARCHAR(20),
        B VARCHAR(20),
        C VARCHAR(20),
        D VARCHAR(20),
        E VARCHAR(20),
        F VARCHAR(20),
        G VARCHAR(20),
        H VARCHAR(20),
        I VARCHAR(20),
        J VARCHAR(20),
        K VARCHAR(20),
        L VARCHAR(20),
        M VARCHAR(20),
        N VARCHAR(20),
        O VARCHAR(20),
        P VARCHAR(20),
        Q VARCHAR(20),
        R VARCHAR(20),
        S VARCHAR(20),
        T VARCHAR(20),
        U VARCHAR(20)
        );"""
    conn.execute(query)
    print ("Table created successfully")

def insert_temp_data(data):
    statement = "INSERT INTO temp_data VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    conn = sqlite3.connect("nba_stats.db")
    conn.executemany(statement, data)
    conn.commit()

def initial_game_data():
    conn = sqlite3.connect("nba_stats.db")  #创建sqlite.db数据库
    print ("open database success")
    conn.execute("drop table IF EXISTS game_data")
    query = """create table IF NOT EXISTS game_data(
        SEASON_ID VARCHAR(20),
        TEAM_ID VARCHAR(20),
        TEAM_ABBREVIATION VARCHAR(20),
        TEAM_NAME VARCHAR(20),
        GAME_ID VARCHAR(20),
        GAME_DATE VARCHAR(20),
        MATCHUP VARCHAR(20),
        WL VARCHAR(20),
        MIN VARCHAR(20),
        PTS VARCHAR(20),
        FGM VARCHAR(20),
        FGA VARCHAR(20),
        FG_PCT VARCHAR(20),
        FG3M VARCHAR(20),
        FG3A VARCHAR(20),
        FG3_PCT VARCHAR(20),
        FTM VARCHAR(20),
        FTA VARCHAR(20),
        FT_PCT VARCHAR(20),
        OREB VARCHAR(20),
        DREB VARCHAR(20),
        REB VARCHAR(20),
        AST VARCHAR(20),
        STL VARCHAR(20),
        BLK VARCHAR(20),
        TOV VARCHAR(20),
        PF VARCHAR(20),
        PLUS_MINUS VARCHAR(20)
        );"""
    conn.execute(query)
    print ("Table created successfully")

def initial_average_data():
    conn = sqlite3.connect("nba_stats.db")  #创建sqlite.db数据库
    print ("open database success")
    conn.execute("drop table IF EXISTS average_data")
    query = """create table IF NOT EXISTS average_data(
        PLAYER_ID VARCHAR(20),
        PLAYER_NAME VARCHAR(20),
        TEAM_ID VARCHAR(20),
        TEAM_ABBREVIATION VARCHAR(20),
        AGE VARCHAR(20),
        GP VARCHAR(20),
        W VARCHAR(20),
        L VARCHAR(20),
        W_PCT VARCHAR(20),
        MIN VARCHAR(20),
        FGM VARCHAR(20),
        FGA VARCHAR(20),
        FG_PCT VARCHAR(20),
        FG3M VARCHAR(20),
        FG3A VARCHAR(20),
        FG3_PCT VARCHAR(20),
        FTM VARCHAR(20),
        FTA VARCHAR(20),
        FT_PCT VARCHAR(20),
        OREB VARCHAR(20),
        DREB VARCHAR(20),
        REB VARCHAR(20),
        AST VARCHAR(20),
        TOV VARCHAR(20),
        STL VARCHAR(20),
        BLK VARCHAR(20),
        BLKA VARCHAR(20),
        PF VARCHAR(20),
        PFD VARCHAR(20),
        PTS VARCHAR(20),
        PLUS_MINUS VARCHAR(20),
        NBA_FANTASY_PTS VARCHAR(20),
        DD2 VARCHAR(20),
        TD3 VARCHAR(20),
        GP_RANK VARCHAR(20),
        W_RANK VARCHAR(20),
        L_RANK VARCHAR(20),
        W_PCT_RANK VARCHAR(20),
        MIN_RANK VARCHAR(20),
        FGM_RANK VARCHAR(20),
        FGA_RANK VARCHAR(20),
        FG_PCT_RANK VARCHAR(20),
        FG3M_RANK VARCHAR(20),
        FG3A_RANK VARCHAR(20),
        FG3_PCT_RANK VARCHAR(20),
        FTM_RANK VARCHAR(20),
        FTA_RANK VARCHAR(20),
        FT_PCT_RANK VARCHAR(20),
        OREB_RANK VARCHAR(20),
        DREB_RANK VARCHAR(20),
        REB_RANK VARCHAR(20),
        AST_RANK VARCHAR(20),
        TOV_RANK VARCHAR(20),
        STL_RANK VARCHAR(20),
        BLK_RANK VARCHAR(20),
        BLKA_RANK VARCHAR(20),
        PF_RANK VARCHAR(20),
        PFD_RANK VARCHAR(20),
        PTS_RANK VARCHAR(20),
        PLUS_MINUS_RANK VARCHAR(20),
        NBA_FANTASY_PTS_RANK VARCHAR(20),
        DD2_RANK VARCHAR(20),
        TD3_RANK VARCHAR(20),
        CFID VARCHAR(20),
        CFPARAMS VARCHAR(20)
        );"""
    conn.execute(query)
    print ("Table created successfully")




def initial_player_game_data():
    conn = sqlite3.connect("nba_stats.db")  #创建sqlite.db数据库
    print ("open database success")
    conn.execute("drop table IF EXISTS player_game_data")
    query = """create table IF NOT EXISTS player_game_data(
        SEASON_ID VARCHAR(20),
        PLAYER_ID VARCHAR(20),
        PLAYER_NAME VARCHAR(20),
        TEAM_ID VARCHAR(20),
        TEAM_ABBREVIATION VARCHAR(20),
        TEAM_NAME VARCHAR(20),
        GAME_ID VARCHAR(20),
        GAME_DATE VARCHAR(20),
        MATCHUP VARCHAR(20),
        WL VARCHAR(20),
        MIN VARCHAR(20),
        PTS VARCHAR(20),
        FGM VARCHAR(20),
        FGA VARCHAR(20),
        FG_PCT VARCHAR(20),
        FG3M VARCHAR(20),
        FG3A VARCHAR(20),
        FG3_PCT VARCHAR(20),
        FTM VARCHAR(20),
        FTA VARCHAR(20),
        FT_PCT VARCHAR(20),
        OREB VARCHAR(20),
        DREB VARCHAR(20),
        REB VARCHAR(20),
        AST VARCHAR(20),
        STL VARCHAR(20),
        BLK VARCHAR(20),
        TOV VARCHAR(20),
        PF VARCHAR(20),
        PLUS_MINUS VARCHAR(20)
        );"""
    conn.execute(query)
    print ("Table created successfully")

def initial_pbp_data():
    conn = sqlite3.connect("nba_stats.db")  #创建sqlite.db数据库
    print ("open database success")
    conn.execute("drop table IF EXISTS pbp_data")
    query = """create table IF NOT EXISTS pbp_data(
        GAME_ID VARCHAR(20),
        EVENTNUM INTEGER,
        EVENTMSGTYPE VARCHAR(20),
        EVENTMSGACTIONTYPE VARCHAR(20),
        PERIOD INTEGER,
        WCTIMESTRING VARCHAR(20),
        PCTIMESTRING VARCHAR(20),
        HOMEDESCRIPTION VARCHAR(20),
        NEUTRALDESCRIPTION VARCHAR(20),
        VISITORDESCRIPTION VARCHAR(20),
        SCORE VARCHAR(20),
        SCOREMARGIN INTEGER,
        PERSON1TYPE INTEGER,
        PLAYER1_ID VARCHAR(20),
        PLAYER1_NAME VARCHAR(20),
        PLAYER1_TEAM_ID VARCHAR(20),
        PLAYER1_TEAM_CITY VARCHAR(20),
        PLAYER1_TEAM_NICKNAME VARCHAR(20),
        PLAYER1_TEAM_ABBREVIATION VARCHAR(20),
        PERSON2TYPE VARCHAR(20),
        PLAYER2_ID VARCHAR(20),
        PLAYER2_NAME VARCHAR(20),
        PLAYER2_TEAM_ID VARCHAR(20),
        PLAYER2_TEAM_CITY VARCHAR(20),
        PLAYER2_TEAM_NICKNAME VARCHAR(20),
        PLAYER2_TEAM_ABBREVIATION VARCHAR(20),
        PERSON3TYPE VARCHAR(20),
        PLAYER3_ID VARCHAR(20),
        PLAYER3_NAME VARCHAR(20),
        PLAYER3_TEAM_ID VARCHAR(20),
        PLAYER3_TEAM_CITY VARCHAR(20),
        PLAYER3_TEAM_NICKNAME VARCHAR(20),
        PLAYER3_TEAM_ABBREVIATION VARCHAR(20),
        VIDEO_AVAILABLE_FLAG VARCHAR(10)
    );"""
    conn.execute(query)
    print ("Table created successfully")
#########

type_list =  ['SpeedDistance','Rebounding','Possessions','CatchShoot','PullUpShot','Defense','Drives','Passing','ElbowTouch','PostTouch','PaintTouch','Efficiency']

class tracking_atr:
    game_day = ""
    season_name = ""
    tracking_type = ""
    season_type = ""

def insert_type_data(tracking_type,data_len,data):
    quote = "?"
    for x in range(data_len-1):
        quote = quote + ",?"
    statement = "INSERT INTO " + tracking_type.lower() +  " VALUES(" + quote + ")"
    conn = sqlite3.connect("nba_stats.db")
    conn.executemany(statement, data)
    conn.commit()


def initial_all_type_data():
    initial_drives_data()
    initial_rebounding_data()
    initial_speed_distance_data()
    initial_possessions_data()
    initial_elbow_touch_data()
    initial_catchshoot_data()
    initial_pullupshot_data()
    initial_defense_data()
    initial_passing_data()
    initial_post_touch_data()
    initial_efficiency_data()
    initial_paint_touch_data()



def initial_speed_distance_data():
    conn = sqlite3.connect("nba_stats.db")  #创建sqlite.db数据库
    print ("open database success")
    conn.execute("drop table IF EXISTS speeddistance")
    query = """create table IF NOT EXISTS speeddistance(
    PLAYER_ID VARCHAR(20),
    PLAYER_NAME VARCHAR(20),
    TEAM_ID VARCHAR(20),
    TEAM_ABBREVIATION VARCHAR(20),
    GP VARCHAR(20),
    W VARCHAR(20),
    L VARCHAR(20),
    MIN VARCHAR(20),
    DIST_FEET VARCHAR(20),
    DIST_MILES VARCHAR(20),
    DIST_MILES_OFF VARCHAR(20),
    DIST_MILES_DEF VARCHAR(20),
    AVG_SPEED VARCHAR(20),
    AVG_SPEED_OFF VARCHAR(20),
    AVG_SPEED_DEF VARCHAR(20),
    GAME_DATE VARCHAR(20)
    );"""
    conn.execute(query)
    print ("Table created successfully")

##########

def initial_rebounding_data():
    conn = sqlite3.connect("nba_stats.db")  #创建sqlite.db数据库
    print ("open database success")
    conn.execute("drop table IF EXISTS rebounding")
    query = """create table IF NOT EXISTS rebounding(
        PLAYER_ID VARCHAR(20),
        PLAYER_NAME VARCHAR(20),
        TEAM_ID VARCHAR(20),
        TEAM_ABBREVIATION VARCHAR(20),
        GP VARCHAR(20),
        W VARCHAR(20),
        L VARCHAR(20),
        MIN VARCHAR(20),
        OREB VARCHAR(20),
        OREB_CONTEST VARCHAR(20),
        OREB_UNCONTEST VARCHAR(20),
        OREB_CONTEST_PCT VARCHAR(20),
        OREB_CHANCES VARCHAR(20),
        OREB_CHANCE_PCT VARCHAR(20),
        OREB_CHANCE_DEFER VARCHAR(20),
        OREB_CHANCE_PCT_ADJ VARCHAR(20),
        AVG_OREB_DIST VARCHAR(20),
        DREB VARCHAR(20),
        DREB_CONTEST VARCHAR(20),
        DREB_UNCONTEST VARCHAR(20),
        DREB_CONTEST_PCT VARCHAR(20),
        DREB_CHANCES VARCHAR(20),
        DREB_CHANCE_PCT VARCHAR(20),
        DREB_CHANCE_DEFER VARCHAR(20),
        DREB_CHANCE_PCT_ADJ VARCHAR(20),
        AVG_DREB_DIST VARCHAR(20),
        REB VARCHAR(20),
        REB_CONTEST VARCHAR(20),
        REB_UNCONTEST VARCHAR(20),
        REB_CONTEST_PCT VARCHAR(20),
        REB_CHANCES VARCHAR(20),
        REB_CHANCE_PCT VARCHAR(20),
        REB_CHANCE_DEFER VARCHAR(20),
        REB_CHANCE_PCT_ADJ VARCHAR(20),
        AVG_REB_DIST VARCHAR(20),
        GAME_DATE VARCHAR(20)
        );"""
    conn.execute(query)
    print ("Table created successfully")

##########

def initial_possessions_data():
    conn = sqlite3.connect("nba_stats.db")  #创建sqlite.db数据库
    print ("open database success")
    conn.execute("drop table IF EXISTS possessions")
    query = """create table IF NOT EXISTS possessions(
        PLAYER_ID VARCHAR(20),
        PLAYER_NAME VARCHAR(20),
        TEAM_ID VARCHAR(20),
        TEAM_ABBREVIATION VARCHAR(20),
        GP VARCHAR(20),
        W VARCHAR(20),
        L VARCHAR(20),
        MIN VARCHAR(20),
        POINTS VARCHAR(20),
        TOUCHES VARCHAR(20),
        FRONT_CT_TOUCHES VARCHAR(20),
        TIME_OF_POSS VARCHAR(20),
        AVG_SEC_PER_TOUCH VARCHAR(20),
        AVG_DRIB_PER_TOUCH VARCHAR(20),
        PTS_PER_TOUCH VARCHAR(20),
        ELBOW_TOUCHES VARCHAR(20),
        POST_TOUCHES VARCHAR(20),
        PAINT_TOUCHES VARCHAR(20),
        PTS_PER_ELBOW_TOUCH VARCHAR(20),
        PTS_PER_POST_TOUCH VARCHAR(20),
        PTS_PER_PAINT_TOUCH VARCHAR(20),
        GAME_DATE VARCHAR(20)
        
        );"""
    conn.execute(query)
    print ("Table created successfully")

##########

def initial_catchshoot_data():
    conn = sqlite3.connect("nba_stats.db")  #创建sqlite.db数据库
    print ("open database success")
    conn.execute("drop table IF EXISTS catchshoot")
    query = """create table IF NOT EXISTS catchshoot(
        PLAYER_ID VARCHAR(20),
        PLAYER_NAME VARCHAR(20),
        TEAM_ID VARCHAR(20),
        TEAM_ABBREVIATION VARCHAR(20),
        GP VARCHAR(20),
        W VARCHAR(20),
        L VARCHAR(20),
        MIN VARCHAR(20),
        CATCH_SHOOT_FGM VARCHAR(20),
        CATCH_SHOOT_FGA VARCHAR(20),
        CATCH_SHOOT_FG_PCT VARCHAR(20),
        CATCH_SHOOT_PTS VARCHAR(20),
        CATCH_SHOOT_FG3M VARCHAR(20),
        CATCH_SHOOT_FG3A VARCHAR(20),
        CATCH_SHOOT_FG3_PCT VARCHAR(20),
        CATCH_SHOOT_EFG_PCT VARCHAR(20),
        GAME_DATE VARCHAR(20)
        );"""
    conn.execute(query)
    print ("Table created successfully")

##########

def initial_pullupshot_data():
    conn = sqlite3.connect("nba_stats.db")  #创建sqlite.db数据库
    print ("open database success")
    conn.execute("drop table IF EXISTS pullupshot")
    query = """create table IF NOT EXISTS pullupshot(
        PLAYER_ID VARCHAR(20),
        PLAYER_NAME VARCHAR(20),
        TEAM_ID VARCHAR(20),
        TEAM_ABBREVIATION VARCHAR(20),
        GP VARCHAR(20),
        W VARCHAR(20),
        L VARCHAR(20),
        MIN VARCHAR(20),
        PULL_UP_FGM VARCHAR(20),
        PULL_UP_FGA VARCHAR(20),
        PULL_UP_FG_PCT VARCHAR(20),
        PULL_UP_PTS VARCHAR(20),
        PULL_UP_FG3M VARCHAR(20),
        PULL_UP_FG3A VARCHAR(20),
        PULL_UP_FG3_PCT VARCHAR(20),
        PULL_UP_EFG_PCT VARCHAR(20),
        GAME_DATE VARCHAR(20)
        );"""
    conn.execute(query)
    print ("Table created successfully")

##########


def initial_defense_data():
    conn = sqlite3.connect("nba_stats.db")  #创建sqlite.db数据库
    print ("open database success")
    conn.execute("drop table IF EXISTS defense")
    query = """create table IF NOT EXISTS defense(
        PLAYER_ID VARCHAR(20),
        PLAYER_NAME VARCHAR(20),
        TEAM_ID VARCHAR(20),
        TEAM_ABBREVIATION VARCHAR(20),
        GP VARCHAR(20),
        W VARCHAR(20),
        L VARCHAR(20),
        MIN VARCHAR(20),
        STL VARCHAR(20),
        BLK VARCHAR(20),
        DREB VARCHAR(20),
        DEF_RIM_FGM VARCHAR(20),
        DEF_RIM_FGA VARCHAR(20),
        DEF_RIM_FG_PCT VARCHAR(20),
        GAME_DATE VARCHAR(20)
        );"""
    conn.execute(query)
    print ("Table created successfully")

##########

def initial_drives_data():
    conn = sqlite3.connect("nba_stats.db")  #创建sqlite.db数据库
    print ("open database success")
    conn.execute("drop table IF EXISTS drives")
    query = """create table IF NOT EXISTS drives(
        PLAYER_ID VARCHAR(20),
        PLAYER_NAME VARCHAR(20),
        TEAM_ID VARCHAR(20),
        TEAM_ABBREVIATION VARCHAR(20),
        GP VARCHAR(20),
        W VARCHAR(20),
        L VARCHAR(20),
        MIN VARCHAR(20),
        DRIVES VARCHAR(20),
        DRIVE_FGM VARCHAR(20),
        DRIVE_FGA VARCHAR(20),
        DRIVE_FG_PCT VARCHAR(20),
        DRIVE_FTM VARCHAR(20),
        DRIVE_FTA VARCHAR(20),
        DRIVE_FT_PCT VARCHAR(20),
        DRIVE_PTS VARCHAR(20),
        DRIVE_PTS_PCT VARCHAR(20),
        DRIVE_PASSES VARCHAR(20),
        DRIVE_PASSES_PCT VARCHAR(20),
        DRIVE_AST VARCHAR(20),
        DRIVE_AST_PCT VARCHAR(20),
        DRIVE_TOV VARCHAR(20),
        DRIVE_TOV_PCT VARCHAR(20),
        DRIVE_PF VARCHAR(20),
        DRIVE_PF_PCT VARCHAR(20),
        GAME_DATE VARCHAR(20)
        );"""
    conn.execute(query)
    print ("Table created successfully")

##########

def initial_passing_data():
    conn = sqlite3.connect("nba_stats.db")  #创建sqlite.db数据库
    print ("open database success")
    conn.execute("drop table IF EXISTS passing")
    query = """create table IF NOT EXISTS passing(
        PLAYER_ID VARCHAR(20),
        PLAYER_NAME VARCHAR(20),
        TEAM_ID VARCHAR(20),
        TEAM_ABBREVIATION VARCHAR(20),
        GP VARCHAR(20),
        W VARCHAR(20),
        L VARCHAR(20),
        MIN VARCHAR(20),
        PASSES_MADE VARCHAR(20),
        PASSES_RECEIVED VARCHAR(20),
        AST VARCHAR(20),
        FT_AST VARCHAR(20),
        SECONDARY_AST VARCHAR(20),
        POTENTIAL_AST VARCHAR(20),
        AST_PTS_CREATED VARCHAR(20),
        AST_ADJ VARCHAR(20),
        AST_TO_PASS_PCT VARCHAR(20),
        AST_TO_PASS_PCT_ADJ VARCHAR(20),
        GAME_DATE VARCHAR(20)
        );"""
    conn.execute(query)
    print ("Table created successfully")

##########

def initial_elbow_touch_data():
    conn = sqlite3.connect("nba_stats.db")  #创建sqlite.db数据库
    print ("open database success")
    conn.execute("drop table IF EXISTS elbowtouch")
    query = """create table IF NOT EXISTS elbowtouch(
        PLAYER_ID VARCHAR(20),
        PLAYER_NAME VARCHAR(20),
        TEAM_ID VARCHAR(20),
        TEAM_ABBREVIATION VARCHAR(20),
        GP VARCHAR(20),
        W VARCHAR(20),
        L VARCHAR(20),
        MIN VARCHAR(20),
        TOUCHES VARCHAR(20),
        ELBOW_TOUCHES VARCHAR(20),
        ELBOW_TOUCH_FGM VARCHAR(20),
        ELBOW_TOUCH_FGA VARCHAR(20),
        ELBOW_TOUCH_FG_PCT VARCHAR(20),
        ELBOW_TOUCH_FTM VARCHAR(20),
        ELBOW_TOUCH_FTA VARCHAR(20),
        ELBOW_TOUCH_FT_PCT VARCHAR(20),
        ELBOW_TOUCH_PTS VARCHAR(20),
        ELBOW_TOUCH_PTS_PCT VARCHAR(20),
        ELBOW_TOUCH_PASSES VARCHAR(20),
        ELBOW_TOUCH_PASSES_PCT VARCHAR(20),
        ELBOW_TOUCH_AST VARCHAR(20),
        ELBOW_TOUCH_AST_PCT VARCHAR(20),
        ELBOW_TOUCH_TOV VARCHAR(20),
        ELBOW_TOUCH_TOV_PCT VARCHAR(20),
        ELBOW_TOUCH_FOULS VARCHAR(20),
        ELBOW_TOUCH_FOULS_PCT VARCHAR(20),
        GAME_DATE VARCHAR(20)
        );"""
    conn.execute(query)
    print ("Table created successfully")

##########

def initial_post_touch_data():
    conn = sqlite3.connect("nba_stats.db")  #创建sqlite.db数据库
    print ("open database success")
    conn.execute("drop table IF EXISTS posttouch")
    query = """create table IF NOT EXISTS posttouch(
        PLAYER_ID VARCHAR(20),
        PLAYER_NAME VARCHAR(20),
        TEAM_ID VARCHAR(20),
        TEAM_ABBREVIATION VARCHAR(20),
        GP VARCHAR(20),
        W VARCHAR(20),
        L VARCHAR(20),
        MIN VARCHAR(20),
        TOUCHES VARCHAR(20),
        POST_TOUCHES VARCHAR(20),
        POST_TOUCH_FGM VARCHAR(20),
        POST_TOUCH_FGA VARCHAR(20),
        POST_TOUCH_FG_PCT VARCHAR(20),
        POST_TOUCH_FTM VARCHAR(20),
        POST_TOUCH_FTA VARCHAR(20),
        POST_TOUCH_FT_PCT VARCHAR(20),
        POST_TOUCH_PTS VARCHAR(20),
        POST_TOUCH_PTS_PCT VARCHAR(20),
        POST_TOUCH_PASSES VARCHAR(20),
        POST_TOUCH_PASSES_PCT VARCHAR(20),
        POST_TOUCH_AST VARCHAR(20),
        POST_TOUCH_AST_PCT  VARCHAR(20),
        POST_TOUCH_TOV VARCHAR(20),
        POST_TOUCH_TOV_PCT VARCHAR(20),
        POST_TOUCH_FOULS VARCHAR(20),
        POST_TOUCH_FOULS_PCT VARCHAR(20),
        GAME_DATE VARCHAR(20)
        
        );"""
    conn.execute(query)
    print ("Table created successfully")

##########


def initial_paint_touch_data():
    conn = sqlite3.connect("nba_stats.db")  #创建sqlite.db数据库
    print ("open database success")
    conn.execute("drop table IF EXISTS painttouch")
    query = """create table IF NOT EXISTS painttouch(
        PLAYER_ID VARCHAR(20),
        PLAYER_NAME VARCHAR(20),
        TEAM_ID VARCHAR(20),
        TEAM_ABBREVIATION VARCHAR(20),
        GP VARCHAR(20),
        W VARCHAR(20),
        L VARCHAR(20),
        MIN VARCHAR(20),
        TOUCHES VARCHAR(20),
        PAINT_TOUCHES VARCHAR(20),
        PAINT_TOUCH_FGM VARCHAR(20),
        PAINT_TOUCH_FGA VARCHAR(20),
        PAINT_TOUCH_FG_PCT VARCHAR(20),
        PAINT_TOUCH_FTM VARCHAR(20),
        PAINT_TOUCH_FTA VARCHAR(20),
        PAINT_TOUCH_FT_PCT VARCHAR(20),
        PAINT_TOUCH_PTS VARCHAR(20),
        PAINT_TOUCH_PTS_PCT VARCHAR(20),
        PAINT_TOUCH_PASSES VARCHAR(20),
        PAINT_TOUCH_PASSES_PCT VARCHAR(20),
        PAINT_TOUCH_AST VARCHAR(20),
        PAINT_TOUCH_AST_PCT VARCHAR(20),
        PAINT_TOUCH_TOV VARCHAR(20),
        PAINT_TOUCH_TOV_PCT VARCHAR(20),
        PAINT_TOUCH_FOULS VARCHAR(20),
        PAINT_TOUCH_FOULS_PCT VARCHAR(20),
        GAME_DATE VARCHAR(20)
        
        );"""
    conn.execute(query)
    print ("Table created successfully")

##########

def initial_efficiency_data():
    conn = sqlite3.connect("nba_stats.db")  #创建sqlite.db数据库
    print ("open database success")
    conn.execute("drop table IF EXISTS efficiency")
    query = """create table IF NOT EXISTS efficiency(
        PLAYER_ID VARCHAR(20),
        PLAYER_NAME VARCHAR(20),
        TEAM_ID VARCHAR(20),
        TEAM_ABBREVIATION VARCHAR(20),
        GP VARCHAR(20),
        W VARCHAR(20),
        L VARCHAR(20),
        MIN VARCHAR(20),
        POINTS VARCHAR(20),
        DRIVE_PTS VARCHAR(20),
        DRIVE_FG_PCT VARCHAR(20),
        CATCH_SHOOT_PTS VARCHAR(20),
        CATCH_SHOOT_FG_PCT VARCHAR(20),
        PULL_UP_PTS VARCHAR(20),
        PULL_UP_FG_PCT VARCHAR(20),
        PAINT_TOUCH_PTS VARCHAR(20),
        PAINT_TOUCH_FG_PCT VARCHAR(20),
        POST_TOUCH_PTS VARCHAR(20),
        POST_TOUCH_FG_PCT VARCHAR(20),
        ELBOW_TOUCH_PTS VARCHAR(20),
        ELBOW_TOUCH_FG_PCT VARCHAR(20),
        EFF_FG_PCT VARCHAR(20),
        GAME_DATE VARCHAR(20)
        );"""
    conn.execute(query)
    print ("Table created successfully")

##########


def initial_shot_detail_data():
    conn = sqlite3.connect("nba_stats.db")  #创建sqlite.db数据库
    print ("open database success")
    conn.execute("drop table IF EXISTS shot_detail_data")
    query = """create table IF NOT EXISTS shot_detail_data(
        GRID_TYPE VARCHAR(20),
        GAME_ID VARCHAR(20),
        GAME_EVENT_ID VARCHAR(20),
        PLAYER_ID VARCHAR(20),
        PLAYER_NAME VARCHAR(20),
        TEAM_ID VARCHAR(20),
        TEAM_NAME VARCHAR(20),
        PERIOD INTEGER,
        MINUTES_REMAINING INTEGER,
        SECONDS_REMAINING INTEGER,
        EVENT_TYPE VARCHAR(20),
        ACTION_TYPE VARCHAR(20),
        SHOT_TYPE VARCHAR(20),
        SHOT_ZONE_BASIC VARCHAR(20),
        SHOT_ZONE_AREA VARCHAR(20),
        SHOT_ZONE_RANGE VARCHAR(20),
        SHOT_DISTANCE VARCHAR(20),
        LOC_X INTEGER,
        LOC_Y INTEGER,
        SHOT_ATTEMPTED_FLAG VARCHAR(20),
        SHOT_MADE_FLAG VARCHAR(20),
        GAME_DATE VARCHAR(20),
        HTM VARCHAR(20),
        VTM VARCHAR(20)
        );"""
    conn.execute(query)
    print ("Table created successfully")
    
def initial_player_info_data():
    conn = sqlite3.connect("nba_stats.db")  #创建sqlite.db数据库
    print ("open database success")
    conn.execute("drop table IF EXISTS player_info_data")
    query = """create table IF NOT EXISTS player_info_data(
        PERSON_ID VARCHAR(20),
        DISPLAY_LAST_COMMA_FIRST VARCHAR(20),
        DISPLAY_FIRST_LAST VARCHAR(20),
        ROSTERSTATUS VARCHAR(20),
        FROM_YEAR VARCHAR(20),
        TO_YEAR VARCHAR(20),
        PLAYERCODE VARCHAR(20),
        TEAM_ID VARCHAR(20),
        TEAM_CITY VARCHAR(20),
        TEAM_NAME VARCHAR(20),
        TEAM_ABBREVIATION VARCHAR(20),
        TEAM_CODE VARCHAR(20),
        GAMES_PLAYED_FLAG VARCHAR(20),
        OTHERLEAGUE_EXPERIENCE_CH VARCHAR(20)
        );"""
    conn.execute(query)
    print ("Table created successfully")


def initial_team_info_data():
    conn = sqlite3.connect("nba_stats.db")  #创建sqlite.db数据库
    print ("open database success")
    conn.execute("drop table IF EXISTS team_info_data")
    query = """create table IF NOT EXISTS team_info_data(
        TEAM_ID VARCHAR(20),
        ABBREVIATION VARCHAR(20),
        YEARFOUNDED VARCHAR(20),
        CITY VARCHAR(20),
        ARENA VARCHAR(20),
        NICKNAME VARCHAR(20),
        ARENACAPACITY VARCHAR(20),
        OWNER VARCHAR(20),
        GENERALMANAGER VARCHAR(20),
        HEADCOACH VARCHAR(20),
        DLEAGUEAFFILIATION VARCHAR(20)
        );"""
    conn.execute(query)
    print ("Table created successfully")

def insert_team_info_data(data):
    statement = "INSERT INTO team_info_data VALUES(?,?,?,?,?,?,?,?,?,?,?)"
    conn = sqlite3.connect("nba_stats.db")
    conn.executemany(statement, data)
    conn.commit()

def insert_shot_detail_data(data):
    statement = "INSERT INTO shot_detail_data VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    conn = sqlite3.connect("nba_stats.db")
    conn.executemany(statement, data)
    conn.commit()

def insert_pbp_data(data):
    statement = "INSERT INTO pbp_data VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    conn = sqlite3.connect("nba_stats.db")
    conn.executemany(statement, data)
    conn.commit()

def insert_player_list(data):
    statement = "INSERT INTO player_info_data VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    conn = sqlite3.connect("nba_stats.db")
    conn.executemany(statement, data)
    conn.commit()

def insert_drives_data(data):
    statement = "INSERT INTO drives VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    conn = sqlite3.connect("nba_stats.db")
    conn.executemany(statement, data)
    conn.commit()

def insert_game_data(data):
    statement = "INSERT INTO game_data VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    conn = sqlite3.connect("nba_stats.db")
    conn.executemany(statement, data)
    conn.commit()


def insert_game_data(data):
    statement = "INSERT INTO game_data VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    conn = sqlite3.connect("nba_stats.db")
    conn.executemany(statement, data)
    conn.commit()

def insert_average_data(data):
    statement = "INSERT INTO average_data VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    conn = sqlite3.connect("nba_stats.db")
    conn.executemany(statement, data)
    conn.commit()

def get_a_game_pbp(game_id):
    conn = sqlite3.connect('nba_stats.db')
    c = conn.cursor()
    statement = "SELECT * from pbp_data where GAME_ID = \"{}\"".format(game_id)
    cursor = c.execute(statement)
    list = []
    for row in cursor:
        list.append(row)
    return list

def get_player_record_data(player_name,column,condition = "DESC"):
    conn = sqlite3.connect('nba_stats.db')
    c = conn.cursor()
    statement = "SELECT * from player_game_data where player_name like \"%{}%\" order by ({}+0) {} limit 1".format(player_name,column,condition)
    print(statement)
    cursor = c.execute(statement)
    list = []
    for row in cursor:
        list.append(row)
    return list

def get_a_shot_detail(game_id,event_num):
    conn = sqlite3.connect('nba_stats.db')
    c = conn.cursor()
    statement = "SELECT * from shot_detail_data where GAME_ID = \"{}\" and GAME_EVENT_ID = \"{}\"".format(game_id,event_num)
    cursor = c.execute(statement)
    list = []
    for row in cursor:
        list.append(row)
    return list

def get_a_colomn_table(table = "player_game_data"):
    conn = sqlite3.connect('nba_stats.db')
    c = conn.cursor()
    statement = "PRAGMA table_info({}})".format(table)
    cursor = c.execute(statement)
    list = []
    for row in cursor:
        list.append(row)
    return list

