#!/usr/bin/env python
#-*-coding:utf-8-*-
"""
numbers.py
Copyright@ takamitu_hamada
version :  June 2,2025
License      :  BSD License
"""
from numbers_list import *
from numbers_rehearsal import *
from loto_list import *
import random,sys,os,math
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#sys.path.append(os.pardir)
#Numbers3
#numbers3クラス
class numbers3(object):
    def __init__(self):
#過去の当選数字全て
        self.full_num3 = [i[1] for i in list3]

#ミニ当選数字と当選回数
        self.full_mini = [i%100 for i in self.full_num3]
        self.full_mini_count = list(zip(self.full_mini,[self.full_mini.count(i) for i in self.full_mini]))

#過去240回のミニ当選数字
        self.mini_240 = [self.full_mini[i] for i in range(240)]
        self.mini_240_count = list(zip(self.mini_240,[self.mini_240.count(i) for i in self.mini_240]))
        self.dic_mini_full = sorted(set(zip([i for i in range(100)],[self.mini_240.count(i) for i in [i for i in range(100)]])))

#ストレート当選数字と当選回数
        self.nums3full = list(zip(self.full_num3,[self.full_num3.count(i) for i in self.full_num3]))

#過去240回のストレート当選数字
        self.num31020 = [self.full_num3[i] for i in range(240)]
        self.num31020_count = list(zip(self.num31020,[self.num31020.count(i) for i in self.num31020]))

#過去240回の各桁数列
        self.num1 = [math.floor(self.num31020[i]/100) for i in range(240)]
        self.num2 = [math.floor(self.num31020[i]%100/10) for i in range(240)]
        self.num3 = [math.floor(self.num31020[i]%100%10) for i in range(240)]

#全ストレート番号
    def make_straight(self):
        rs3 = [i for i in xrange(1000)]
        return rs3
#全ボックス番号
    def make_box(self,rs3):
        rs3a = [math.floor(i/100) for i in rs3]
        rs3b = [math.floor(i%100/10) for i in rs3]
        rs3c = [math.floor(i%100%10) for i in rs3]
        rs3d = [sorted([rs3a[i],rs3b[i],rs3c[i]]) for i in range(len(rs3))]
        rs3 = [i[0]*100+i[1]*10+i[2] for i in rs3d]
        return rs3

#過去特定回数に出現したミニ数字
    def make_numbersmini(self,num):
        self.e = [math.floor(self.full_num3[i]%100) for i in range(num)]
        return self

#ナンバーズ3ミニ
#makeMiniNumber
#100までの数列を作成
    def makeMiniNumber3(self):
        e = [i for i in range(100)]
        return e

#過去特定回数のミニ当選数字を削除
    def delstmini(self,num,e):
        for i in [self.full_mini[j] for j in range(num)]:
            try:e.remove(i)
            except:e
        return e
        
#過去特定回数以上出現していないミニの当選数字を削除
    def delbeforemini(self,num,e):
        full_mini = [math.floor(i%100) for i in self.full_num3]
        nf_mini = sorted(set([full_mini[i] for i in range(len(self.full_num3)-1) if full_mini.index(full_mini[i]) >= num]))
        dbm = [i for i in e for j in nf_mini if i == j]
        for i in dbm:
            try:e.remove(i)
            except:e
        return e

#ナンバーズ3ストレート・ボックス・セット
#makeNumber
#ミニの予想数字をベースに３桁の数字を作成
    def makeNumber3(self,e):
        return [i*100+j for i in [math.floor(k/100) for k in sorted(set([self.full_num3[m] for m in range(20)]))] for j in e]

#過去特定回数のストレート数字を削除
    def delst(self,num,rs3):
        for i in [self.full_num3[j] for j in range(num)]:
            try:rs3.remove(i)
            except:rs3
        return rs3
#過去特定回数のボックスの当選数字を削除
    def delbox(self,reverse_num,rs3):
        num_a = [math.floor(self.full_num3[i]/100) for i in range(reverse_num)]
        num_b = [math.floor(self.full_num3[i]%100/10) for i in range(reverse_num)]
        num_c = [math.floor(self.full_num3[i]%100%10) for i in range(reverse_num)]

        reverse1 = [(num_a[i]*100+num_c[i]*10+num_b[i]) for i in range(reverse_num)]
        reverse2 = [(num_b[i]*100+num_a[i]*10+num_c[i]) for i in range(reverse_num)]
        reverse3 = [(num_b[i]*100+num_c[i]*10+num_a[i]) for i in range(reverse_num)]
        reverse4 = [(num_c[i]*100+num_b[i]*10+num_a[i]) for i in range(reverse_num)]
        reverse5 = [(num_c[i]*100+num_a[i]*10+num_b[i]) for i in range(reverse_num)]
        reverse_n3 = reverse1+reverse2+reverse3+reverse4+reverse5
        reverse_n3 = sorted(set(reverse_n3))
        for i in reverse_n3:
            try:rs3.remove(i)
            except:rs3
        return rs3
#過去1度も出現していない数字を削除
    def delzero(self,rs3):
        box = sorted(set(self.make_box(self.make_straight())))
        fullbox = sorted(set(self.make_box(self.full_num3)))
        dic_3b = sorted(set(zip(box,[fullbox.count(i) for i in box])))
        dz3 = [i for i in rs3 for j in dic_3b if j[1] == 0 and i == j[0]]
        for i in dz3:
            try:rs3.remove(i)
            except:rs3
        return rs3
#ゾロ目を削除
    def delzoro3(self,rs3):
        zoro3 = [i*100+i*10+i for i in range(10)]
        for i in zoro3:
            try:rs3.remove(i)
            except:rs3
        return rs3
#過去特定回数以上出現していない当選数字を削除
    def delbefore(self,num,rs3):
        nf = sorted(set([i for i in self.full_num3 if self.full_num3.index(i) >= num]))
        dbm = [i for i in rs3 for j in nf if i == j]
        dbm2 = self.make_box(dbm)
        for i in dbm2:
            try:rs3.remove(i)
            except:rs3
        return rs3

#Numbers 4
#Numbers4クラス
class numbers4(object):
    def __init__(self):
#過去のストレート当選数字
        self.full_num34 = [i[1] for i in list4]

#過去全てのストレート数字と当選回数
        self.nfc100 = list(zip(self.full_num34,[self.full_num34.count(i) for i in self.full_num34]))

#過去240回の各桁数列
        self.nums4240 = [self.full_num34[i] for i in range(240)]
        self.num1a = [math.floor(self.nums4240[i]/1000) for i in range(240)]
        self.num2a = [math.floor(self.nums4240[i]%1000/100) for i in range(240)]
        self.num3a = [math.floor(self.nums4240[i]%1000%100/10) for i in range(240)]
        self.num4a = [math.floor(self.nums4240[i]%1000%100%10) for i in range(240)]

#全ストレート番号
    def make_straight(self):
        rs = [i for i in range(10000)]
        return rs

#全ボックス番号
    def make_box(self,rs):
        rsa = [math.floor(i/1000) for i in rs]
        rsb = [math.floor(i%1000/100) for i in rs]
        rsc = [math.floor(i%1000%100/10) for i in rs]
        rsd = [math.floor(i%1000%100%10) for i in rs]
        rse = [sorted([rsa[i],rsb[i],rsc[i],rsd[i]]) for i in range(len(rs))]
        rs = [i[0]*1000+i[1]*100+i[2]*10+i[3] for i in rse]
        return rs
#1番目の数字と2番目の数字の2桁数列と3番目の数字と4番目の数字の2桁数列の組み合わせによるナンバーズ4の数列
    def make_numbers4xxx(self):
        num4mini_base =  sorted(set([self.full_num34[m] for m in range(21,50)]))
        num4mini01 = [math.floor(i/100) for i in num4mini_base]
        num4mini02 = [math.floor(j%100) for j in num4mini_base]
        rs = sorted(set([i*100+j for i in num4mini01 for j in num4mini02]))
        return rs

    def make_numbers4xxx2(self):
        num4mini_base =  sorted(set([self.full_num34[m] for m in range(240)]))
        num4yyy01 = [k for k in range(100)]
        num4yyy02 = [l for l in range(100)]
        num4mini01 = [math.floor(i/100) for i in num4mini_base]
        num4mini02 = [math.floor(j%100) for j in num4mini_base]
        for i in num4mini01:
            try:
                num4yyy01.remove(i)
            except:pass
        for j in num4mini02:
            try:
                num4yyy02.remove(i)
            except:pass
        
        rs = sorted(set([i*100+j for i in num4yyy01 for j in num4yyy02]))
        return rs

#過去のストレート数字を削除
    def delst(self,rs):
        for i in self.full_num34:
            try:
                rs.remove(i)
            except:pass
        return rs
#ボックスの当選数字を削除
    def delbox(self,reverse_num,rs):
        num_a = [math.floor(self.full_num34[i]/1000) for i in range(reverse_num)]
        num_b = [math.floor(self.full_num34[i]%1000/100) for i in range(reverse_num)]
        num_c = [math.floor(self.full_num34[i]%1000%100/10) for i in range(reverse_num)]
        num_d = [math.floor(self.full_num34[i]%1000%100%10) for i in range(reverse_num)]

        reverse_a = [(num_a[i]*1000+num_b[i]*100+num_d[i]*10+num_c[i]) for i in range(reverse_num)]
        reverse_b = [(num_a[i]*1000+num_c[i]*100+num_b[i]*10+num_d[i]) for i in range(reverse_num)]
        reverse_c = [(num_a[i]*1000+num_c[i]*100+num_d[i]*10+num_b[i]) for i in range(reverse_num)]
        reverse_d = [(num_a[i]*1000+num_d[i]*100+num_b[i]*10+num_c[i]) for i in range(reverse_num)]
        reverse_e = [(num_a[i]*1000+num_d[i]*100+num_c[i]*10+num_b[i]) for i in range(reverse_num)]
        reverse_f = [(num_b[i]*1000+num_a[i]*100+num_c[i]*10+num_d[i]) for i in range(reverse_num)]
        reverse_g = [(num_b[i]*1000+num_a[i]*100+num_d[i]*10+num_c[i]) for i in range(reverse_num)]
        reverse_h = [(num_b[i]*1000+num_d[i]*100+num_a[i]*10+num_c[i]) for i in range(reverse_num)]
        reverse_i = [(num_b[i]*1000+num_d[i]*100+num_c[i]*10+num_a[i]) for i in range(reverse_num)]
        reverse_j = [(num_b[i]*1000+num_c[i]*100+num_a[i]*10+num_d[i]) for i in range(reverse_num)]
        reverse_k = [(num_b[i]*1000+num_c[i]*100+num_d[i]*10+num_a[i]) for i in range(reverse_num)]
        reverse_l = [(num_c[i]*1000+num_a[i]*100+num_b[i]*10+num_d[i]) for i in range(reverse_num)]
        reverse_m = [(num_c[i]*1000+num_a[i]*100+num_d[i]*10+num_b[i]) for i in range(reverse_num)]
        reverse_n = [(num_c[i]*1000+num_b[i]*100+num_a[i]*10+num_d[i]) for i in range(reverse_num)]
        reverse_o = [(num_c[i]*1000+num_b[i]*100+num_d[i]*10+num_a[i]) for i in range(reverse_num)]
        reverse_p = [(num_c[i]*1000+num_d[i]*100+num_a[i]*10+num_b[i]) for i in range(reverse_num)]
        reverse_q = [(num_c[i]*1000+num_d[i]*100+num_b[i]*10+num_a[i]) for i in range(reverse_num)]
        reverse_r = [(num_d[i]*1000+num_a[i]*100+num_b[i]*10+num_c[i]) for i in range(reverse_num)]
        reverse_s = [(num_d[i]*1000+num_a[i]*100+num_c[i]*10+num_b[i]) for i in range(reverse_num)]
        reverse_t = [(num_d[i]*1000+num_b[i]*100+num_a[i]*10+num_c[i]) for i in range(reverse_num)]
        reverse_u = [(num_d[i]*1000+num_b[i]*100+num_c[i]*10+num_a[i]) for i in range(reverse_num)]
        reverse_v = [(num_d[i]*1000+num_c[i]*100+num_a[i]*10+num_b[i]) for i in range(reverse_num)]
        reverse_w = [(num_d[i]*1000+num_c[i]*100+num_b[i]*10+num_a[i]) for i in range(reverse_num)]
        reverse_n4 = reverse_a+reverse_b+reverse_c+reverse_d+reverse_e+reverse_f+reverse_g+reverse_h+reverse_i+reverse_j+reverse_k+reverse_l+reverse_m+reverse_n+reverse_o+reverse_p+reverse_q+reverse_r+reverse_s+reverse_t+reverse_u+reverse_v+reverse_w

        for i in reverse_n4:
            try:rs.remove(i)
            except:rs
        return rs

#ゾロ目を削除
    def delzoro4(self,rs):
        for i in [i*1000+i*100+i*10+i for i in range(10)]:
            try:rs.remove(i)
            except:rs
        return rs

#トリプルの数字を削除
    def deltriple(self,rs):
        rs3z = []
        for i in range(10):
            for j in range(10):
                try:
                    rs3z.append(i*1000+i*100+i*10+j)
                    rs3z.append(j*1000+i*100+i*10+i)
                    rs3z.append(i*1000+j*100+i*10+i)
                    rs3z.append(i*1000+i*100+j*10+i)
                except:pass
        rs3z = set(sorted(rs3z))
        for i in rs3z:
            try:
                rs.remove(i)
            except:pass
        return rs
#ダブルの数字を削除
    def deldouble(self,rs):
        d4 = []
        for i in range(10):
            for j in range(10):
                try:
                    d4.append(i*1000+i*100+j*10+j)
                    d4.append(i*1000+j*100+i*10+j)
                    d4.append(i*1000+j*100+j*10+i)
                    d4.append(j*1000+i*100+i*10+j)
                    d4.append(j*1000+i*100+j*10+i)
                    d4.append(j*1000+j*100+i*10+i)
                except:pass
        d4 = set(sorted(d4))
        for i in d4:
            try:
                rs.remove(i)
            except:pass
        return rs
#過去特定回数以上出現していない当選数字を削除
    def delbefore(self,num,rs):
        nf = sorted(set([i for i in self.full_num34 if self.full_num34.index(i) >= num]))
        dbm = [i for i in rs for j in nf if i == j]
        dbm2 = self.make_box(dbm)
        for i in dbm2:
            try:rs.remove(i)
            except:rs
        return rs


#ナンバーズ予想スクリプト
class allnumbers(object):
    def __init__(self):
#Numbers3予想
        n3=numbers3()
#mini
        ee = n3.makeMiniNumber3()
        n3.delstmini(100,ee)
        n3.delbeforemini(200,ee)
        e = ee
        #e = sorted(set([random.choice(ee) for i in range(20)]))
        n3a = sorted(set(zip(e,[n3.full_mini.count(i) for i in e])))
#straight
        rs3 = n3.makeNumber3(e)
        n3.delst(240,rs3)
        rs3 = sorted(set(n3.make_box(rs3)))
        n3.delbox(20,rs3)
        n3.delzoro3(rs3)
        #rs3 = set(sorted([random.choice(rs3) for i in range(10)]))
        n3b = sorted(set(zip(rs3,[n3.make_box(n3.full_num3).count(i) for i in rs3])))
#Numbers4予想
        n4 = numbers4()
        #rs = n4.make_numbers4xxx2()
        rs = n4.make_straight()
        n4.delst(rs)
        n4.delbox(240,rs)
        n4.delzoro4(rs)
        n4.deltriple(rs)
        n4.deldouble(rs)
        rs = sorted(set(n4.make_box(rs)))
        #n4a = sorted(set(zip(rs,[n4.make_box(n4.full_num34).count(i) for i in rs])))

#File writing
        sssmini = str([format(i[0],'02') for i in n3a])
        #print(str([i[0] for i in n3a]) + "\n")
        sss3 = str([format(i[0],'03') for i in n3b])
        print(str(sss3)+"\n")
        sss4 = str([format(i,'04') for i in rs])
        print(str(sss4) + "\n")
        with open("numbers.txt","w") as f:
#ミニ予想数字
            f.write("◇ナンバーズ3ミニ予想数字\n"+ str([i[0] for i in n3a]) + "\n"+str(len([i[0] for i in n3a]))+"個\n")

#Numbers3予想数字
            f.write("◇ナンバーズ3予想数字\n"+sss3+"\n"+str(len([i[0] for i in n3b]))+"個\n")
            
#Numbers4予想数字
            f.write("◇ナンバーズ4予想数字\n"+ sss4 + "\n" + str(len([i for i in rs])) + "個\n")
            f.close()
            print("Finish")

#ロト class
class loto(object):
    def __init__(self):
        pass
    def six(self):
        loto_base = [i for i in range(1,44)]
        yn = len(loto6)
        la = [loto6[i][0] for i in range(yn)]
        lb = [loto6[i][1] for i in range(yn)]
        lc = [loto6[i][2] for i in range(yn)]
        ld = [loto6[i][3] for i in range(yn)]
        le = [loto6[i][4] for i in range(yn)]
        lf = [loto6[i][5] for i in range(yn)]
        la1,lb1,lc1,ld1,le1,lf1=loto_base,loto_base,loto_base,loto_base,loto_base,loto_base
        for k in la:
              try:
                  la1.remove(k)
              except:
                  pass
        for k in lb:
              try:
                  lb1.remove(k)
              except:
                  pass
        for k in lc:
              try:
                  lc1.remove(k)
              except:
                  pass
        for k in ld:
              try:
                  ld1.remove(k)
              except:
                  pass
        for k in le:
              try:
                  le1.remove(k)
              except:
                  pass
        for k in lf:
              try:
                  lf1.remove(k)
              except:
                  pass
        lss = sorted(set(la+lb+lc+ld+le+lf))
        for j in lss:
            try:
                lss.remove(j)
            except:
                lss
        for  j2 in deleteloto6:
            try:
                lss.remove(j2)
            except:
                lss
        #print(lss)
        lss2 = sorted(set(la1+lb1+lc1+lc1+ld1+le1))
        for j3 in lss:
            try:
                lss.remove(j3)
            except:
                lss
        for  j4 in deleteloto6:
            try:
                lss2.remove(j4)
            except:
                lss2
        #print(lss2)
        loto_e = []
        while len(loto_e) < 6:
            la2 = random.randrange(1,44)
            lb2 = random.randrange(1,44)
            lc2 = random.randrange(1,44)
            ld2 = random.randrange(1,44)
            le2 = random.randrange(1,44)
            lf2 = random.randrange(1,44)
            if(la2 == la[0] and la2 == la[1]):
                la2 = random.choice(la)
            if(lb2 == lb[0] and lb2 == lb[1]):
                lb2 = random.choice(lb)
            if(lc2 == lc[0] and lc2 == lc[1]):
                lc2 = random.choice(lc)
            #if(ld2 == ld[0] and ld2 == ld[1]):
            #    ld2 = random.choice(ld)
            #if(le2 == le[0] and le2 == le[1]):
            #    le2 = random.choice(le)
            #if(lf2 == lf[0] and lf2 == lf[1]):
            #    lf2 = random.choice(lf)
            loto_e = sorted(set([la2,lb2,lc2,ld2,le2,lf2]))
        print(loto_e)
        return loto_e
    def mini(self):
        miniloto_base = [i for i in range(1,32)]
        ynmini = len(lotomini)
        la = [lotomini[i][0] for i in range(ynmini)]
        lb = [lotomini[i][1] for i in range(ynmini)]
        lc = [lotomini[i][2] for i in range(ynmini)]
        ld = [lotomini[i][3] for i in range(ynmini)]
        le = [lotomini[i][4] for i in range(ynmini)]
        la1,lb1,lc1,ld1,le1=miniloto_base,miniloto_base,miniloto_base,miniloto_base,miniloto_base
        for k in la:
              try:
                  la1.remove(k)
              except:
                  pass
        for k in lb:
              try:
                  lb1.remove(k)
              except:
                  pass
        for k in lc:
              try:
                  lc1.remove(k)
              except:
                  pass
        for k in ld:
              try:
                  ld1.remove(k)
              except:
                  pass
        for k in le:
              try:
                  le1.remove(k)
              except:
                  pass
        ltt = sorted(set(la+lb+lc+ld+le))
        for j in bonus:
              try:
                  ltt.remove(j)
              except:
                  ltt
        for j2 in deleteminiloto:
              try:
                  ltt.remove(j2)
              except:
                  ltt
        ltt2 = sorted(set(la1+lb1+lc1+ld1+le1))
        for j3 in bonus:
              try:
                  ltt2.remove(j3)
              except:
                  ltt2
        for j4 in ltt2:
              try:
                  ltt2.remove(j4)
              except:
                  ltt2
        mini_e = []
        while len(mini_e) < 5:
            la2 = random.choice(ltt)
            lb2 = random.choice(ltt2)
            lc2 = continuation2[0]
            ld2 = continuation2[1]
            le2 = continuation2[2]
            if(la2 == la[0] and la2 == la[1]):
                la2 = random.choice(la)
            if(lb2 == lb[0] and lb2 == lb[1]):
                lb2 = random.choice(lb)
            if(lc2 == lc[0] and lc2 == lc[1]):
                lc2 = random.choice(lc)
            if(ld2 == ld[0] and ld2 == ld[1]):
                ld2 = random.choice(ld)
            if(le2 == le[0] and le2 == le[1]):
                le2 = random.choice(le)
            mini_e =sorted(set([la2,lb2,lc2,ld2,le2]))
        print(mini_e)
        return mini_e

class allloto(object):
    def __init__(self):
        lx=loto()
#File writing
        fl = open("loto.txt","w")
        fl.write("◇ロト予想数字\n")
        fl.write(str(lx.six()) + "\n")
        fl.write("◇ミニロト予想数字\n")
        fl.write(str(lx.mini()) + "\n")
        fl.close()
        print("Finish")

if __name__ == "__main__":
    allnumbers()
    #allloto()
    #from download_data import *
    #dd = download_data()
    #dd.download_html()
    #print("Finish")
    
