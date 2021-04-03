from src.ngram import Ngram


with open("wiki-data.txt",encoding="utf8") as myfile:
    data=myfile.readlines()

train_data=' '.join(data[:13341])
test_data=' '.join(data[13341:])
test_data=test_data.split('.')

print(train_data)
print(test_data)

ngrams=[]
for i in range(5):
    ngrams.append(Ngram(i+1,train_data))
"""
outfile = open('File_Results.txt','w',encoding="utf8")
outfile.write("{}{}{}{}{}{}\n".format("1-gram".ljust(40), "2-gram".ljust(40),"3-gram".ljust(40),"4-gram".ljust(40),"5-gram","sentence".ljust(40), ))
for i in test_data:
    if i!='\n':
        i = i.replace("\n", "")
        print("testing",i)
        outfile.write("{}{}{}{}{}{}\n".format(str(ngrams[0].calc_perplexity_of(i)).ljust(40), str(ngrams[1].calc_perplexity_of(i)).ljust(40),str(ngrams[2].calc_perplexity_of(i)).ljust(40),str(ngrams[3].calc_perplexity_of(i)).ljust(40),str(ngrams[4].calc_perplexity_of(i)).ljust(40),i))
outfile.close()
"""
outfile = open('rand_out.txt','w',encoding="utf8")
outfile.write("{}".format(ngrams[4].random5()))
outfile.close()
