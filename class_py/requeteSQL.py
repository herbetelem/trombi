# coding: utf-8

import psycopg2

class SQL():

    def __init__(self) :

        self.MyConnection = ""     
        self.MyResult = ""

    def DBConnect(self):
        """
            Connect to Database
        """
        self.MyConnection = None

        try:
            self.MyConnection = psycopg2.connect(
                host="localhost",
                database="trombi",
                user="postgres",
                password="group12"
            )
        except(Exception, psycopg2.DatabaseError) as Error:
            # error
            print(f"\nCannot connect to specified DB :\n{Error}")
        return self.MyConnection

    def ExecuteQuery(self,
        MyQuery):
        """
            Execute Specified SQL query
            return query result
        """
        self.MyResult = None

        if self.MyConnection is not None:
            # create DB cursor
            MyCursor = self.MyConnection.cursor()
            # execute query
            MyCursor.execute(MyQuery)
            # get result
            self.MyResult = MyCursor.fetchall()
            # close cursor
            MyCursor.close()
        return self.MyResult

    def requeteSQL(self) :
        
        self.MyConnection = self.DBConnect()

        MyQuery = (
            "SELECT * " +
            "FROM stagiaire " )
        self.MyResult = self.ExecuteQuery(MyQuery)

    def requeteSQL_course(self, stagiaire) :
        
        self.MyConnection = self.DBConnect()

        MyQuery = (
            "SELECT parcours.parcours " +
            "FROM parcours " +
            f"WHERE id_stagiaire = {stagiaire}")
        Result = self.ExecuteQuery(MyQuery)

        return Result