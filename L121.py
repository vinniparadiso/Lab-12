#Bethany Berlage and Vinni Paradiso
import re
def get_hashtag_ranking(input_sentence):
    hashtag_list=re.findall(r"#\w+", input_sentence)
    hashtag_count={}
    for hashtag in hashtag_list:
        if hashtag in hashtag_count:
            hashtag_count[hashtag]+=1
        else:
            hashtag_count[hashtag]=1
    def get_frequency(hashtag_count_pair):
        return hashtag_count_pair[1]
    sorted_hashtags=sorted(hashtag_count.items(),key=get_frequency, reverse=True)
    output_list=[hashtag for (hashtag,count) in sorted_hashtags]
    return output_list
my_sentence="I love #Python and #MachineLearning, but #DataScience is also great. #Python #Python #Python #DataScience"
my_list=get_hashtag_ranking(my_sentence)
print(my_list)
