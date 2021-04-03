from collections import Counter
import sys,math,random
from src.helper import check_corpus,text_to_syllable,lower
from nltk.util import ngrams
import pickle
class Ngram:
    def __init__(self,n,corpus):
        self.n=n
        self.ngram=self.count_ngrams(self.create_ngrams(corpus))
        print(n, "Gram Data Created.")
        self.count_of_counts()
        self.gt_smoothing()
        print("smoothing")
        self.calc_probability()

    def create_ngrams(self, corpus):
        crps = lower(corpus)
        crps = check_corpus(crps)
        crps = text_to_syllable(crps)
        return list(ngrams(crps, self.n))

    def count_ngrams(self,ngrams):
        self.N = 0;
        ngram_dict = {}
        n=self.n
        for i in ngrams:
            if i[0:n - 1] in ngram_dict and i[n - 1:] in ngram_dict[i[0:n - 1]]:
                ngram_dict[i[0:n - 1]][i[n - 1:]] += 1
            elif i[0:n - 1] in ngram_dict:
                ngram_dict[i[0:n - 1]][i[n - 1:]] = 1
            else:
                ngram_dict[i[0:n - 1]] = {}
                ngram_dict[i[0:n - 1]][i[n - 1:]] = 1
            self.N+=1
        return ngram_dict;

    def count_of_counts(self):
        self.Ns=dict()
        for i in self.ngram:
            for j in self.ngram[i]:
                if self.ngram[i][j] in self.Ns:
                    self.Ns[self.ngram[i][j]]+=1
                else:
                    self.Ns[self.ngram[i][j]]=1
    def gt_smoothing(self):
        K=5
        for i in self.ngram:
            for j in self.ngram[i]:
                if self.ngram[i][j]>=1 and self.ngram[i][j]<=K:
                    c=self.ngram[i][j]
                    Nc=self.Ns[c] if c in self.Ns else 1
                    c1=c+1
                    Nc1=self.Ns[c1] if c1 in self.Ns else 1
                    Nk1=self.Ns[K+1] if K+1 in self.Ns else 1
                    N1=self.Ns[1] if 1 in self.Ns else 1
                    self.ngram[i][j]=((c1*(Nc1/Nc)) - (c*(((K+1)*Nk1)/N1))) / (1-(((K+1)*Nk1)/N1))

    def calc_probability(self):
        self.prob={}
        for i in self.ngram:
            if i not in self.prob:
                self.prob[i] = {}
            for j in self.ngram[i]:
                self.prob[i][j]=self.ngram[i][j]/self.N

    def calc_probability_of(self,text):
        text = lower(text)
        crps = check_corpus(text)
        crps = text_to_syllable(crps)
        res=0
        if len(crps)<self.n:
            return 1.0
        text_gram=list(ngrams(crps, self.n))
        for i in text_gram:
            if i[0:self.n-1] in self.ngram and i[self.n-1:] in self.ngram[i[0:self.n-1]]:
                res+=math.log(self.prob[i[0:self.n-1]][i[self.n-1:]],10)
            else:
                res+=math.log(self.Ns[1]/self.N,10)
        res=math.exp(res)
        return res

    def calc_perplexity_of(self,text):
        prob=self.calc_probability_of(text)
        if prob==1 or prob==0:
            return None
        perp=(1/prob)**(1/self.n)
        return perp

    def random5(self):
        ret = ""
        if self.n == 1:
            k = Counter(self.prob[()])
            spacce=k[' ',]
            del k[' ',]
            i = 1
            while i <= 15:
                x=k.most_common(1)[0][0]
                ret += x[0]
                del k[x]
                if i==1:
                    k[' ',]=spacce
                i += 1
            return ret
        else:
            max_i, max_J = random.choice(list(self.prob.items()))
            max_J, prob = random.choice(list(max_J.items()))
            max_J=max_J[0]
            ret=''.join(max_i[0:self.n])+max_J
            for i in range(500):
                if self.n>2:
                    ind = ', '.join('\'{}\''.format(t) for t in max_i[1:self.n])
                    ind += ' ,\'' + max_J + '\''
                else:
                    ind ='\'' + max_J + '\','
                k=Counter(self.prob[(eval(ind))]).most_common(1)[0]
                max_i=(eval(ind))
                max_J=k[0][0]
                ret +=max_J
            return ret