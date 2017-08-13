
def fetchRecords():
        import psycopg2
        conn = psycopg2.connect(database="tcount", user="postgres", password="pass", port="5432")
        cur = conn.cursor()
        cur.execute('''SELECT * FROM tweetwordcount ORDER BY count DESC;''')
        records = cur.fetchall()
        conn.commit()
        conn.close()

        return records


def main():
        from optparse import OptionParser
        parser = OptionParser()
        parser.add_option("-v", "--verbose", action = "store_true")

        (options, args) = parser.parse_args()
        recs = fetchRecords()
        #print(recs)
        #print(list(args))
        if len(args) > 0:
                list(args)
                minhist = int(args[0].split(',')[0])
                maxhist = int(args[0].split(',')[1])

                for i in recs:
                        if (int(i[1]) >= int(minhist)) and (int(i[1]) <= int(maxhist)):
                                print(i[0] + ': ' + str(i[1]))
        else:
                print("Error!!! Fix yo Hist FUNC")





if __name__ == '__main__':
        main()
