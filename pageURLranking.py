import math

from nltk import word_tokenize
from matplotlib import pyplot as plt
def make_file_with_max_DCG(lines):
    lines.sort(reverse=True)
    file1 = open("max_DCG_file.txt", "w")  # write mode
    count_dict={'0':0,'1':0,'2':0,'3':0,'4':0}
    for x in lines:
        print(x)

        file1.write(x)
        count_dict[x[0]]=count_dict[x[0]]+1
    print(count_dict)

    file1.close()



def make_file_with_dec_tf_idf(lines):
    lines_temp={}
    print(len(lines))
    for x in lines:
        # print(x.split()[76])
        # lines_temp.append(x.split()[76][3:]+x)
        lines_temp[x]=float(x.split()[76][3:])
        # print(x.split()[76][3:])
    # lines_temp.sort(reverse=True)
    print(lines_temp)

    i=0
    k=0
    m=0
    # print(len(lines_temp))
    temp=sorted(lines_temp.items(), key = lambda kv:(kv[1], kv[0]),reverse=True)

    for x in temp:
        # print(x[0].split()[0])
        # print(x,lines_temp[x][0])
        # print(x[0][0])

        if x[0][0]!='0':
            k=k+1


        # else:
            # print(lines_temp[x][0])
            # m=m+1
        lines[i]=x[0]
        i=i+1
    precision=[]
    recall=[]
    i=0
    j=0
    # print(k,len(lines),m)
    for x in lines:
        i=i+1
        if x[0]!='0':
            j=j+1
            # print(x[0])
        precision.append(j/i)
        recall.append(j/k)
    print(precision)
    print(recall)
    plt.plot(recall, precision)
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Precision-Recall Curve')
    plt.show()




def compute_nDCG(lines,k):

    dcg=0
    i=0

    for x in lines:
        i=i+1
        # print(x)

        # dcg=dcg+int(x.split()[0])/math.log2(i+1)
        reli=int(x.split()[0])
        dcg=dcg+(2 ** reli-1)/math.log2(i+1)
        # print(int(x.split()[0]) / math.log10(i + 1))
        if(i==k):
            # print(i)
            break
    lines.sort(reverse=True)
    print(len(lines))
    # print(lines)
    idcg=0
    i=0
    for x in lines:
        i=i+1
        # print(x)
        # idcg=idcg+float(x.split()[0])/math.log2(i+1)
        reli = int(x.split()[0])
        idcg=idcg+(2 ** reli-1)/math.log2(i+1)
        # print(int(x.split()[0])/math.log10(i+1))
        if(i==k):
            break
    if k==len(lines):
        k="Whole Dataset"

    print("nDCG at",k,":",dcg/idcg)
    print("dcg:",dcg,"idcg:",idcg)




def load_data():
    path="/home/gaurav/Desktop/IIITD/IR/Assignments/Assignment3/IR-assignment-3-data.txt"
    # f = open(path , encoding='ISO-8859-1')
    print("Reading....")
    file1 = open(path, 'r',encoding='ISO-8859-1')
    Lines = file1.readlines()
    # list_tokens=word_tokenize(f.read())
    # print(list_tokens,path)
    # print(Lines)
    print(len(Lines))
    lines=[]
    i=0
    for x in Lines:
        # print(len((x.split())))
        if(x.split()[1]=='qid:4'):
            # print(x)
            lines.append(x)
        # lines.append(x.split())
        # print(lines[i])
        # print(i)
        i = i + 1
    # lines=list(set(lines))

    make_file_with_max_DCG(lines)

    # compute_DCG(lines, 5)
    lines1=lines.copy()
    compute_nDCG(lines1,50) # DCG at 50
    lines2=lines.copy()
    compute_nDCG(lines2, len(lines))
    make_file_with_dec_tf_idf(lines)








load_data()
