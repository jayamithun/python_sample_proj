''' Interactive Python project which simulates an Electronic Voting Machine (EVM) with the Following :     (i)    To insert candidate's name, symbol & group name from user for voting purpose.     (ii)   To accept maximum 10 candidate from an area. (Here I have specified other candidates with an <empty> text.)     (iii)  To allow voting by the votes (single vote per person).     (iv)   To store the poll result in different file for different candidates.     (v)    To display the winner and total number of votes.     (vi)   To display the result candidate wise.     (vii)  As on pilot basis, can record maximum 100 votes. (Here I have specified only 3 votes, which can be            changed to 100)    The Electronic Voting Machine (EVM) should not allow voter to vote more than once.'''from tkinter import *import mysql.connector as sql""" Module tkinter is a library  for Graphical User Interface (GUI) programming in python. All the graphical work in this program have been done using this module only. """""" Module mysql.connector is used for the connection of Python program with mysql database. So that I can store andupdate the data related to the application in a secured manner. """class vote :    def __init__(self, win) :        self.win = win        self.win.geometry("800x650+500+50")        self.win.title("  Electronic Voting Machine  ")        self.win.configure(bg = "#D4E1E3")        self.election = []        self.number_voter = 0        def leader() :            ''' The function leader() creates a frame for the participating candidates. It ask for a group name,            leader and symbol for the specific groups contesting election from user. It also have two buttons with            two different function. One is to Cancel the work and other redirects to another function named            leader_enter_function(). '''            self.frame_leader = Frame(self.win, width = 800, height = 650, bg = "#B88FDE")            self.frame_leader.place(x = 0, y = 0)            num_leader = 0            if num_leader <= 10 :                self.leader_group = StringVar()                self.leader_name = StringVar()                self.leader_logo = StringVar()                self.leader_group_label = Label(self.frame_leader, text = " Enter the Name of your Group : ",                                                bg = "#B88FDE", fg = "black", font = ('Bahnschrift SemiLight', 15))                self.leader_name_label = Label(self.frame_leader, text = " Enter the Name of the Candidate : ",                                               bg = "#B88FDE", fg = "black", font = ('Bahnschrift SemiLight', 15))                self.leader_logo_label = Label(self.frame_leader, text = " Enter the symbol for your Group : ",                                               bg = "#B88FDE", fg = "black", font = ('Bahnschrift SemiLight', 15))                self.leader_group_entry  = Entry(self.frame_leader, textvariable = self.leader_group, bd = 0,width = 30)                self.leader_name_entry = Entry(self.frame_leader, textvariable = self.leader_name, bd = 0, width = 30)                self.leader_logo_entry = Entry(self.frame_leader, textvariable = self.leader_logo, bd = 0, width = 30)                self.leader_group_label.place(x = 100, y = 210)                self.leader_name_label.place(x = 100, y = 310)                self.leader_logo_label.place(x = 100, y = 410)                self.leader_group_entry.place(x = 430, y = 215)                self.leader_name_entry.place(x = 430, y = 315)                self.leader_logo_entry.place(x = 430, y = 415)                self.leader_enter = Button(self.frame_leader, text = "  Enter  ", bd = 0, fg = "white", bg = "black",                                           command = leader_enter_function, width = 20, height = 3)                cancel = Button(self.frame_leader, text = " Cancel ", bd = 0, fg = "white", bg = "black",                                command = cancel_func, width = 20, height = 3)                cancel.place(x = 410, y = 540)                self.leader_enter.place(x = 225, y = 540)                num_leader += 1        def leader_enter_function() :            ''' The function leader_enter_function() first check that the Entry box are filled or not. If they are            Empty the it goes to if part and shows a error frame. Otherwise it extract the data from leader() and            stores it into a list named self.election. After that it again call the main() or the first page.'''            if self.leader_group_entry.get() == "" or self.leader_name_entry.get() == "" or self.leader_logo_entry.get () == "" :                error_txt = " COLUMNS CANNOT be Empty. "                error_frame_handling(self.frame_leader, hgt = 100, txt = error_txt, flag = False)            else :                candidate = []                candidate.append(self.leader_group_entry.get())                candidate.append(self.leader_name_entry.get())                candidate.append(self.leader_logo_entry.get())                candidate.append(0)                if len(self.election) <= 10 :                    self.election.append(candidate)                    error_txt = " You have been SUCCESSFULLY Registered. "                    error_frame_handling(self.frame_leader, hgt = 100, txt = error_txt, flag = True)                else :                    error_txt = " Maximum candidate have been enrolled. "                    error_frame_handling(self.frame_leader, hgt = 100, txt = error_txt, flag = True)        def coountdown(time, fab, ali) :            ''' The function coountdown() is to remove any frame after a specific time. Generally, it hides a given            frame (eg: error frames) after a given time. '''            if ali == True :                if time == -1:                    fab.destroy()                    try :                        if self.frame_voter :                            self.frame_voter.place_forget()                            main()                        elif self.frame_main_vote :                            self.frame_main_vote.place_forget()                            main()                    except AttributeError :                        if self.frame_leader :                            self.frame_leader.destroy()                            main()                    finally :                        try :                            if self.frame_leader :                                self.frame_leader.destroy()                                main()                        except AttributeError :                            main()                        finally :                            main()                else :                    fab.after(500, coountdown, time - 1, fab, True)            else :                if time == -1 :                    fab.place_forget()                else :                    fab.after(500, coountdown, time - 1, fab, False)        def error_frame_handling(frame, hgt, txt, flag) :            ''' The function is called when any error occurred. It generally creates a frame and shows the specific            error to the user, so that it can be rectified. And hide the frame using the coountdown().'''            frame_local_error = Frame(frame, width = 800, height = hgt + 50, bg = "#D1D5B7")            frame_local_error.place(x = 0, y = 250)            error_label = Label(frame_local_error, text = txt, font = ('Bahnschrift SemiLight', 11, 'bold'))            error_label.configure(fg = "black", bg = "#D1D5B7")            error_label.place(x = 240, y = 60)            if flag == True :                coountdown(5, frame_local_error, True)            else :                coountdown(5,frame_local_error, False)        def voter() :            ''' The function voter() ask for for an Unique Id or Voter Id of the user for the security purpose of            the election. '''            voter_id = StringVar()            self.frame_voter = Frame(self.win, width = 800, height = 650, bg = "#851085")            self.frame_voter.place(x = 0, y = 0)            self.voter_id_label = Label(self.frame_voter, text = " VOTER  ID : ", bg = "#851085", fg = "#EDF314",                                        font = ('Agency FB', 20))            self.voter_id_label.place(x = 280, y = 265)            self.voter_id_entry = Entry(self.frame_voter, textvariable = voter_id, bd = 0, width = 28)            self.voter_id_entry.place(x = 390, y = 279)            self.voter_id_enter = Button(self.frame_voter, bd = 0, command = main_voting_page, text = "  Enter  ",                                         fg = "white", bg = "black", width = 15, height = 3)            cancel = Button(self.frame_voter, text = " Cancel ", bd = 0, fg = "white", bg = "black",                            command = cancel_func, width = 15, height = 3)            self.voter_id_enter.place(x = 305, y = 350)            cancel.place(x = 440, y = 350)        def main_voting_page() :            ''' The function main_voting_page() first checks the Unique Id from MySql Server, if matched then only            the next frame is placed otherwise not. It show all the groups with their leader names & symbols            participating in the election. If it is less than 10, then it creates <empty> labels for the extra space .            And also packs 10 CheckButtons to place vote. And if any error occurred then it will show it to user. '''            self.db = sql.connect(host = "localhost", user = "root", passwd = "2012", database = "election")            self.cur = self.db.cursor()            self.cur.execute("select * from voter_list where voter_id = '%s'" % (str(self.voter_id_entry.get())))            rud = self.cur.fetchall()            if rud :                self.cur.execute("select state from voter_list where voter_id = '%s'"% (str(self.voter_id_entry.get())))                if_not = self.cur.fetchone()                if if_not[0] == "false" :                    self.frame_main_vote = Frame(self.frame_voter, width = 800, height = 650, bg = "#F1CD51")                    self.frame_main_vote.place(x = 0, y = 0)                    while len(self.election) != 10 and len(self.election) != 0 :                        if len(self.election) <= 10 :                            self.election.append(["<empty>", "", "", 0])                        elif len(self.election) > 10 :                            self.election.pop()                    try :                        self.var_1 = IntVar()                        self.var_2 = IntVar()                        self.var_3 = IntVar()                        self.var_4 = IntVar()                        self.var_5 = IntVar()                        self.var_6 = IntVar()                        self.var_7 = IntVar()                        self.var_8 = IntVar()                        self.var_9 = IntVar()                        self.var_10 = IntVar()                        self.group_1 = Checkbutton(self.frame_main_vote, text = self.election[0][2], onvalue = 1,                                                   offvalue = 0, variable = self.var_1, bg = "#F1CD51", fg = "black")                        self.group_2 = Checkbutton(self.frame_main_vote, text = self.election[1][2], onvalue = 1,                                                   offvalue = 0, variable = self.var_2, bg = "#F1CD51", fg = "black")                        self.group_3 = Checkbutton(self.frame_main_vote, text = self.election[2][2], onvalue = 1,                                                   offvalue = 0, variable = self.var_3, bg = "#F1CD51", fg = "black")                        self.group_4 = Checkbutton(self.frame_main_vote, text = self.election[3][2], onvalue = 1,                                                 offvalue = 0, variable = self.var_4, bg = "#F1CD51", fg = "black")                        self.group_5 = Checkbutton(self.frame_main_vote, text = self.election[4][2], onvalue = 1,                                                   offvalue = 0, variable = self.var_5, bg = "#F1CD51", fg = "black")                        self.group_6 = Checkbutton(self.frame_main_vote, text = self.election[5][2], onvalue = 1,                                                   offvalue = 0, variable = self.var_6, bg = "#F1CD51", fg = "black")                        self.group_7 = Checkbutton(self.frame_main_vote, text = self.election[6][2], onvalue = 1,                                                   offvalue = 0, variable = self.var_7, bg = "#F1CD51", fg = "black")                        self.group_8 = Checkbutton(self.frame_main_vote, text = self.election[7][2], onvalue = 1,                                                   offvalue = 0, variable = self.var_8, bg = "#F1CD51", fg = "black")                        self.group_9 = Checkbutton(self.frame_main_vote, text = self.election[8][2], onvalue = 1,                                                  offvalue = 0, variable = self.var_9, bg = "#F1CD51", fg = "black")                        self.group_10 = Checkbutton(self.frame_main_vote, text = self.election[9][2], onvalue = 1,                                                    offvalue = 0, variable = self.var_10, bg = "#F1CD51", fg = "black")                        self.group_1.place(x = 300, y = 110)                        self.group_2.place(x = 300, y = 165)                        self.group_3.place(x = 300, y = 220)                        self.group_4.place(x = 300, y = 275)                        self.group_5.place(x = 300, y = 330)                        self.group_6.place(x = 300, y = 385)                        self.group_7.place(x = 300, y = 440)                        self.group_8.place(x = 300, y = 495)                        self.group_9.place(x = 300, y = 550)                        self.group_10.place(x = 300, y = 605)                        gr_name = Label(self.frame_main_vote, text = " GROUP NAME ", bg = "#DEBB43", fg = "black",                                           font = ('Bahnschrift SemiLight', 10))                        gr_ld_name = Label(self.frame_main_vote, text = " LEADER NAME ", bg = "#DEBB43", fg = "black",                                           font = ('Bahnschrift SemiLight', 10))                        gr_symbol = Label(self.frame_main_vote, text = " GROUP SYMBOL ", bg = "#DEBB43", fg = "black",                                           font = ('Bahnschrift SemiLight', 10))                        gr_name.place(x = 50, y = 20)                        gr_ld_name.place(x = 47, y = 40)                        gr_symbol.place(x = 140, y = 20)                        count = 0                        for leaders in self.election :                            lob_grp = Label(self.frame_main_vote, text = leaders[0], bg = "#F1CD51", fg = "#22A26A",                                            font = ('Calibri Light', 12))                            lob_nm = Label(self.frame_main_vote, text = leaders[1], bg = "#F1CD51", fg = "#22A26A",                                           font = ('Calibri Light', 12))                            lob_sym = Label(self.frame_main_vote, text = leaders[2], bg = "#F1CD51", fg = "#22A26A",                                            font = ('Calibri Light', 12))                            lob_grp.place(x = 50, y = 100 + count)                            lob_nm.place(x = 50, y = 120 + count)                            lob_sym.place(x = 155, y = 100 + count)                            count = count + 55                    except AttributeError :                        error_txt = " No candidate enrolled for the Election. "                        error_frame_handling(self.frame_voter, hgt = 100, txt = error_txt, flag = True)                    except IndexError :                        error_txt = " No candidate enrolled for the Election. "                        error_frame_handling(self.frame_voter, hgt = 100, txt = error_txt, flag = True)                    else :                        self.btn_submit = Button(self.frame_main_vote, text = "  SUBMIT  ", bd = 0,                                                 command = initializing_vote, bg = "black", fg = "white", width = 15,                                                 height = 3)                        cancel = Button(self.frame_main_vote, text = " Cancel ", bd = 0, fg = "white", bg = "black",                                        command = cancel_func, width = 15, height = 3)                        self.btn_submit.place(x = 420, y = 330)                        cancel.place(x = 560, y = 330)                else :                    error_txt = " Your VOTE is ALREADY REGISTERED. "                    error_frame_handling(self.frame_voter, hgt = 100, txt = error_txt, flag = True)            else :                error_txt = " You are not Registered in the voter list. "                error_frame_handling(self.frame_voter, hgt = 100, txt = error_txt, flag = True)        def initializing_vote() :            ''' The function initializing_vote() handle all type of errors possible in the voting frame. And it            stores the individual votes in the list self.election. '''            self.vote_result = [int(self.var_1.get()), int(self.var_2.get()), int(self.var_3.get()),                                int(self.var_4.get()), int(self.var_5.get()), int(self.var_6.get()),                                int(self.var_7.get()), int(self.var_8.get()), int(self.var_9.get()),                                int(self.var_10.get())]            count = 0            for voti in range (0, len(self.vote_result)) :                if self.vote_result[voti] != 0 :                    count = count + 1                    self.get = voti            if count > 1 :                error_txt = " You CANNOT Select more than ONE Group "                error_frame_handling(self.frame_main_vote, hgt = 100, txt = error_txt, flag = False)            elif count < 1 :                error_txt = " You have NOT Select ANY Group "                error_frame_handling(self.frame_main_vote, hgt = 100, txt = error_txt, flag = False)            else :                if self.election[self.get][0] == "<empty>" :                    error_txt = " This is a EMPTY Group. You CANNOT Vote this Group "                    error_frame_handling(self.frame_main_vote, hgt = 100, txt = error_txt, flag = False)                else :                    ''' Here the MySql table is updated so that the user with same Id cannot Vote again. It updates the                     column of the for that Unique Id. '''                    self.election[self.get][3] += 1                    error_txt = " You have been Voted SUCCESSFULLY "                    error_frame_handling(self.frame_main_vote, hgt = 100, txt = error_txt, flag = True)                    self.db = sql.connect(host = "localhost", user = "root", passwd = "18180612", database = "election")                    self.cur = self.db.cursor()                    self.cur.execute("update voter_list set state = 'true' where voter_id = '{}'".format                                     (str(self.voter_id_entry.get())))                    self.db.commit()                    self.db.close()                    self.number_voter += 1        def main() :            ''' The function main() is the first page of this application. It shows two option, one is for leaders            and  other is for voters who want to give votes to their representatives. Before that it checks number            of votes placed if it is greater than given number then it show the election result, otherwise it            continues asking for votes. '''            if self.number_voter < 3 :                btn_leader = Button(self.win, text = " Want to be a leader ? ", bg = "#20B4CB", fg = "black", bd = 0,                                    command = leader, width = 20, height = 10, font = ('Bahnschrift SemiLight', 12))                btn_voter = Button(self.win, text = " If you are a voter. ", bg = "#20B4CB", fg = "black", bd = 0,                                   command = voter, width = 20, height = 10, font = ('Bahnschrift SemiLight', 12))                btn_leader.place(x = 200, y = 225)                btn_voter.place(x = 450, y = 225)            else :                self.final_frame = Frame(self.win, width = 800, height = 650, bg = "lightblue")                self.final_frame.place(x = 0, y = 0)                end_label = Label(self.final_frame, text = " ELECTION ENDS ", fg = "black", bg = "lightblue",                                  font = ('Arial Narrow', 24, 'bold'))                end_label.place(x = 312, y = 200)                cancel = Button(self.final_frame, text = " Cancel ", bd = 0, fg = "white", bg = "black",                                command = cancel_func, width = 15, height = 3)                btn_result = Button(self.final_frame, text = " View Results ", fg = "white", bg = "black",                                    width = 15, height = 3, command = view_result)                btn_result.place(x = 305, y = 320)                cancel.place(x = 440, y = 320)        def view_result() :            ''' The function view_result() creates a frame which shows total votes of each group with the a label            Winner in the side of winning group. And three buttons are also packed in frame. One is Back which            redirect the user to the last frame, one is cancel button and last one is exit button which update the            MySql table and delete all the data that have been updated during the execution of this program. '''            self.all_votes = []            for votes in self.election:                self.all_votes.append(votes[3])            self.result_frame = Frame(self.final_frame, width = 800, height = 650, bg = "#81A796")            self.result_frame.place(x = 0, y = 0)            total_win_votes = max(self.all_votes)            gr_name = Label(self.result_frame, text = " GROUP NAME ", bg = "#81A796", fg = "black",                            font = ('Bahnschrift SemiLight', 10))            gr_ld_name = Label(self.result_frame, text = " LEADER NAME ", bg = "#81A796", fg = "black",                               font = ('Bahnschrift SemiLight', 10))            gr_symbol = Label(self.result_frame, text = " GROUP SYMBOL ", bg = "#81A796", fg = "black",                              font = ('Bahnschrift SemiLight', 10))            total_vt = Label(self.result_frame, text = " TOTAL VOTES ", bg = "#81A796", fg = "black",                               font = ('Bahnschrift SemiLight', 10))            gr_name.place(x = 50, y = 20)            gr_ld_name.place(x = 47, y = 40)            gr_symbol.place(x = 140, y = 20)            total_vt.place(x = 300, y = 20)            count = 0            i = 0            for everygroup in range(0, len(self.all_votes)) :                if self.all_votes[everygroup] == total_win_votes :                    lob_grp = Label(self.result_frame, text = self.election[0 + i][0], bg = "#81A796",                                    fg = "#DAE829", font = ('Calibri Light', 12))                    lob_nm = Label(self.result_frame, text = self.election[0 + i][1], bg = "#81A796",                                   fg = "#DAE829", font = ('Calibri Light', 12))                    lob_sym = Label(self.result_frame, text = self.election[0 + i][2], bg = "#81A796",                                    fg = "#DAE829", font = ('Calibri Light', 12))                    lob_vt = Label(self.result_frame, text = self.all_votes[everygroup], bg = "#81A796",                                    fg = "#DAE829", font = ('Calibri Light', 12))                    lob_winner = Label(self.result_frame, text = " WINNER OF THE ELECTION ", bg = "#81A796",                                    fg = "#DAE829", font = ('Calibri Light', 12, 'bold'))                    lob_grp.place(x = 50, y = 100 + count)                    lob_nm.place(x = 50, y = 120 + count)                    lob_sym.place(x = 155, y = 100 + count)                    lob_vt.place(x = 300, y = 100 + count)                    lob_winner.place(x = 400, y = 100 + count)                else :                    lob_grp = Label(self.result_frame, text = self.election[0 + i][0], bg = "#81A796",                                    fg = "#DAE829", font = ('Calibri Light', 12))                    lob_nm = Label(self.result_frame, text = self.election[0 + i][1], bg = "#81A796",                                   fg = "#DAE829", font = ('Calibri Light', 12))                    lob_sym = Label(self.result_frame, text = self.election[0 + i][2], bg = "#81A796",                                    fg ="#DAE829", font = ('Calibri Light', 12))                    lob_vt = Label(self.result_frame, text = self.all_votes[everygroup], bg = "#81A796",                                   fg = "#DAE829", font = ('Calibri Light', 12))                    lob_grp.place(x = 50, y = 100 + count)                    lob_nm.place(x = 50, y = 120 + count)                    lob_sym.place(x = 155, y = 100 + count)                    lob_vt.place(x = 300, y = 100 + count)                count = count + 55                i = i + 1            btn_details = Button(self.result_frame, text = " Save in Files ", bg = "black", fg = "white",                                 command = file_handling, width = 15, height = 3)            btn_exit = Button(self.result_frame, text = " EXIT ", bg = "black", fg = "white",                                 command = cancel_func, width = 15, height = 3)            btn_back = Button(self.result_frame, text = " Back ", bd = 0, fg = "white", bg = "black",                                command = main, width = 15, height = 3)            btn_details.place(x = 680, y = 240)            btn_exit.place(x = 680, y = 400)            btn_back.place(x = 680, y = 320)        def file_handling() :            ''' The function file_handling() creates and save all the data related to every groups participating in            the election in text file and save it in the present directory in the name of their groups.'''            self.file_list = []            for each in range(0, len(self.election)):                if self.election[each][0] != "<empty>" :                    self.file_list.append(self.election[each])                else :                    pass            total_win_votes = max(self.all_votes)            for group in self.file_list :                with open('{}.txt'.format(str(group[0])), 'w') as file_object :                    file_object.write(" GROUP NAME / SYMBOL   : {},   {} \n".format(group[0], group[2]))                    file_object.write(" GROUP LEADER        : {} \n ".format(group[1]))                    file_object.write(" TOTAL VOTES         : {} \n".format(group[3]))                    if group[3] == total_win_votes :                        file_object.write(" WINNER OF THE ELECTION. ")            error_txt = " FILES have been SAVED in the PRESENT DIRECTORY. "            error_frame_handling(self.result_frame, hgt = 100, txt = error_txt, flag = False)        def cancel_func():            ''' The function cancel_func() is a cancel function which deletes all the frame or removes all the            command whenever it is called in the program. '''            try :                if self.result_frame :                    self.db = sql.connect(host="localhost", user="root", passwd="2012", database="election")                    self.cur = self.db.cursor()                    self.cur.execute("update voter_list set state = 'false';")                    self.db.commit()                    self.db.close()                    self.win.quit()            except AttributeError :                try :                    if self.final_frame :                        self.final_frame.place_forget()                        vote(window)                except AttributeError :                    try:                        if self.frame_main_vote:                            self.frame_main_vote.place_forget()                            self.frame_voter.place_forget()                    except AttributeError :                        try:                            if self.frame_voter:                                self.frame_voter.place_forget()                        except AttributeError :                            try:                                if self.frame_leader  :                                    self.frame_leader.place_forget()                            except AttributeError :                                if self.frame_voter :                                    self.frame_voter.place_forget()                            finally :                                main()                        finally :                            main()                    finally :                        main()                finally :                    pass            else :                vote(window)        main()if __name__ == "__main__" :    window = Tk()    vote(window)    window.mainloop()