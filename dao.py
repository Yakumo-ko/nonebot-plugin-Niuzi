from typing import Union, Dict, Tuple, List, Any

from nonebot import get_driver

from .config import Config
from .entiry import Lovers, NiuZi
from .utils.Mysql import Sql



class LoversDAO:
    # sql table name
    __LOVERS: str = "lovers"

    __CREAT_LOVERS: str = """\
            CREATE TABLE IF NOT EXISTS `{table_name}` (                          
                `qq` BIGINT UNIQUE NOT NULL,`target` BIGINT     
            )
            """.format(table_name = __LOVERS)


    def __init__(self) -> None:
        conf = Config.parse_obj(get_driver().config)
        self.sql: Sql = Sql(
                conf.host, 
                conf.port, 
                conf.user, 
                conf.password, 
                conf.database
            )


        self.sql.executeNotQuerySql(self.__CREAT_LOVERS)

    def findloversByQQ(self, qq: str) -> Union[Lovers, None]:
        sql: str = "select * from `{tb_name}` where `qq`='{qq}'".format(
                    tb_name = self.__LOVERS,
                    qq = qq
                )

        res: Union[Tuple[Dict[str, Any]], None]= self.sql.executeQuerySql(sql)

        return Lovers(**res[0]) if res!=None else None

    def getAll(self) -> Union[List[Lovers], None]:
        sql : str = f"select * from `{self.__LOVERS}`"

        rows: Union[Tuple[Dict[str, Any]], None]= self.sql.executeQuerySql(sql)

        if rows == None:
            return rows

        res: List[Lovers] = [Lovers(**row) for row in rows]
        
        return res

    def insert(self, lovers: Lovers) -> bool:
        sql: str =  "INSERT INTO `{table_name}` \
        (qq, target) VALUE\
        ({qq}, {target})".format(
                    qq = lovers.qq,
                    sex = lovers.target,
                    table_name =  self.__LOVERS
                )

        return self.sql.executeNotQuerySql(sql)

    def update(self, lovers: Lovers) -> bool:
        sql: str = """ \
            UPDATE `{table_name}` SET  
                        `qq` = {qq}, 
                        `target` = {target}, 
                    WHERE `qq` = {qq}
            """.format(
                    qq = lovers.qq,
                    target = lovers.target,
                    table_name =  self.__LOVERS
                )

        return self.sql.executeNotQuerySql(sql)

    def delete(self, lovers: Lovers) -> bool:
        sql: str = "DELETE  FROM `{table_name}` WHERE `qq`= {qq}".format(
                    qq=lovers.qq,
                    table_name =  self.__LOVERS
                )

        return self.sql.executeNotQuerySql(sql)


class NiuziDAO:
    # sql table name
    __NIUZI_INFO: str = "niuzi_info"

    # sql 
    __CREAT_NIUZI_INFO: str =  """\
            CREATE TABLE IF NOT EXISTS `{table_name}` (                 
                    `qq` BIGINT UNIQUE NOT NULL,                
                    `name` TEXT, `length` FLOAT,                
                    `sex` INTEGER DEFAULT 0,                    
                    `level` INT DEFAULT 0,                      
                    `points` INT DEFAULT 0, PRIMARY KEY (`qq`)  
                )
            """.format(table_name = __NIUZI_INFO)

    def __init__(self) -> None:
        conf = Config.parse_obj(get_driver().config)
        self.sql: Sql = Sql(
                conf.host, 
                conf.port, 
                conf.user, 
                conf.password, 
                conf.database
            )


        self.sql.executeNotQuerySql(self.__CREAT_NIUZI_INFO)

    def findNiuziByQQ(self, qq: str) -> Union[NiuZi, None]:
        sql: str = "select * from `{tb_name}` where `qq`='{qq}'".format(
                    tb_name = self.__NIUZI_INFO,
                    qq = qq
                )

        res: Union[Tuple[Dict[str, Any]], None]= self.sql.executeQuerySql(sql)

        return NiuZi(**res[0]) if res!=None else None

    def getAll(self) -> Union[List[NiuZi], None]:
        sql : str = f"select * from `{self.__NIUZI_INFO}`"

        rows: Union[Tuple[Dict[str, Any]], None]= self.sql.executeQuerySql(sql)

        if rows == None:
            return rows

        res: List[NiuZi] = [NiuZi(**row) for row in rows]
        
        return res

    def insert(self, niuzi: NiuZi) -> bool:
        sql: str =  "INSERT INTO `{table_name}` \
        (qq,name,length,sex) VALUE\
        ({qq}, {name}, {lenght}, {sex})".format(
                    qq = niuzi.owner,
                    name = niuzi.name,
                    lenght = niuzi.length,
                    sex = niuzi.sex,
                    table_name = self.__NIUZI_INFO
                )

        return self.sql.executeNotQuerySql(sql)

    def update(self, niuzi: NiuZi) -> bool:
        sql: str = """ \
            UPDATE `{table_name}` SET  
                        `sex` = {sex}, 
                        `name` = {name}, 
                        'lenght' ={length},
                    WHERE `qq` = {qq}
            """.format(
                    sex = niuzi.sex,
                    name = niuzi.name,
                    length = niuzi.length,
                    qq = niuzi.owner,
                    table_name = self.__NIUZI_INFO
                )

        return self.sql.executeNotQuerySql(sql)

    def delete(self, niuzi: NiuZi) -> bool:
        sql: str = "DELETE  FROM `{table_name}` WHERE `qq`= {qq}".format(
                    qq=niuzi.owner,
                    table_name = self.__NIUZI_INFO
                )

        return self.sql.executeNotQuerySql(sql)