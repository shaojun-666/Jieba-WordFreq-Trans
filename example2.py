import jieba.posseg as pos
text="当第一缕温润的风轻拂过脸颊，春天便悄然而至了。"
seg=pos.cut(text)
# for i in seg:
#     print(i,end=" ")
lst=[x.word for x in seg if x.flag=='n']
print(lst)
from jieba import analyse as ana
import jieba
text="""影片的主角米格，是一个对音乐充满热爱的小男孩，然而他出生在一个视音乐为洪水猛兽的制鞋家族。家人的强烈反对与米格内心对音乐梦想的炽热追求形成了激烈冲突，这种冲突构成了故事开篇的主要张力。在一年一度的亡灵节，米格意外穿越到了亡灵世界，就此展开了一段充满惊喜与感动的冒险。
亡灵世界的设定堪称一绝，皮克斯团队凭借其卓越的想象力和精湛的制作技术，打造出了一个五彩斑斓、热闹非凡的死后世界。这里有金字塔般的建筑、奇装异服的亡灵，还有那由万寿菊铺就的通往人间的道路，每一个细节都充满了墨西哥文化的独特魅力。在这个世界里，死亡不再是冰冷和悲伤的代名词，而是另一种形式的延续，只有当世上再无人记得你时，才是真正的死亡。这种对死亡的独特诠释，无疑给观众带来了全新的思考视角。
米格在亡灵世界中邂逅了落魄乐手埃克托，随着剧情的推进，我们发现埃克托竟然是米格的曾曾祖父。影片巧妙地通过层层悬念与反转，揭开了家族往事的真相。原来，米格家族对音乐的厌恶源于曾曾祖父埃克托为追求音乐梦想而 “抛弃” 家庭的误解，而真正的罪魁祸首是虚伪的歌神德拉库斯。德拉库斯为了名利，不仅窃取了埃克托的作品，还将其杀害。真相大白的那一刻，观众的情绪被彻底点燃，对德拉库斯的厌恶与对埃克托的同情交织在一起。
在主题表达上，《寻梦环游记》巧妙地将梦想与亲情融合。米格在追求音乐梦想的道路上，虽然遭遇了家人的阻拦，但在亡灵世界的经历让他深刻认识到亲情的珍贵。而家人在了解了埃克托的真实遭遇后，也理解了米格对音乐的热爱，最终给予了他支持。这种梦想与亲情的和解，传递出温暖而积极的信息：梦想与亲情并非水火不容，它们可以相互理解、相互成就。
音乐在影片中起到了至关重要的作用。主题曲《Remember Me》以不同的风格和演绎贯穿始终，每一次响起都恰到好处地推动着剧情发展，引发观众强烈的情感共鸣。当米格用这首歌唤醒太奶奶可可对父亲埃克托的记忆时，相信很多观众都忍不住潸然泪下。音乐在这里不仅仅是一种艺术表达，更是连接生者与逝者、传递爱与思念的桥梁。
从制作层面来看，《寻梦环游记》的画面精美绝伦，色彩搭配和谐而富有冲击力，无论是亡灵世界的华丽场景，还是现实世界中墨西哥小镇的风土人情，都被描绘得栩栩如生。角色形象设计独特，每个亡灵都有其鲜明的个性特征，通过细腻的表情和动作，让观众能够深刻感受到他们的情感变化。
总的来说，《寻梦环游记》是一部近乎完美的动画电影。它用奇幻的故事包裹着深刻的情感与哲理，让观众在欢笑与泪水中重新审视梦想、亲情与死亡。它提醒着我们，要勇敢追求自己的梦想，同时也要珍惜身边的亲人，因为爱与记忆，永远不会消逝"""
keyWords=ana.extract_tags(text,topK=10,withWeight=True)
print("关键词有：")
for keyWord in keyWords:
    print("{:<6} weight:{:4.2f}".format(keyWord[0],keyWord[1]))
wordList=jieba.lcut(text)
def openFileAsList(filePath):
    f=open(filePath,'r',encoding='utf_8')
    lst=f.readline()
    f.close()
    return lst
count={}
for word in wordList:
    if len(word)==1:
        continue
    elif word not in openFileAsList("excludeWord.txt"):
        count[word]=count.get(word,0)+1
allKeyWords=list(count)
allKeyWords.sort(key=lambda x:x[1],reverse=True)
f=open("keyWords_Freq.txt","w+",encoding='utf_8')
topk=int(input("前几个词？\n"))
for i in range(0,topk+1):
    f.write("{}\t{}\n".format(allKeyWords[i][0],allKeyWords[i][1]))
f.close()