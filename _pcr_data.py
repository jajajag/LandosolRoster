'''公主连接Re:dive的游戏数据'''

UnavailableChara = {
    1072,   # 可萝爹
    1073,   # 拉基拉基
    1102,   # 泳装大眼
    1183,   # 星弓星
    1184,   # 星弓栞
    1204,   # 小小甜心美美
    1205,   # 小小甜心禊
    1206,   # 小小甜心镜华
    1217,   # 秋乃(秋乃&咲恋)
    1218,   # 咲恋(秋乃&咲恋)
    1243,   # 安(安&古蕾雅)
    1244,   # 古蕾雅(安&古蕾雅)
}








'''角色名称

遵照格式： id: [台服官译简体, 日文原名, 英文名(罗马音), (B服官译), 常见别称, 带错别字的别称等] (<-依此顺序)
若暂无台服官译则用日文原名占位，一律使用半角括号
'''
CHARA_NAME = {
    1000: ["未知角色", "未知キャラ", "Unknown"],
    1001: ["日和", "ヒヨリ", "Hiyori", "日和莉", "猫拳", "东山", "🐱👊"],
    1002: ["优衣", "ユイ", "Yui", "种田", "普田", "由衣", "结衣", "ue", "↗↘↗↘"],
    1003: ["怜", "レイ", "Rei", "剑圣", "普怜", "伶"],
    1004: ["禊", "ミソギ", "Misogi", "未奏希", "炸弹", "炸弹人", "熊孩子", "💣"],
    1005: ["茉莉", "マツリ", "Matsuri", "跳跳虎", "老虎", "虎", "跳刀虎", "🐅"],
    1006: ["茜里", "アカリ", "Akari", "妹法", "阿卡丽", "妹妹法"],
    1007: ["宫子", "ミヤコ", "Miyako", "布丁", "布", "幽灵", "🍮"],
    1008: ["雪", "ユキ", "Yuki", "小雪", "镜子", "镜法", "伪娘", "男孩子", "男孩纸", "雪哥"],
    1009: ["杏奈", "アンナ", "Anna", "中二", "煤气罐"],
    1010: ["真步", "マホ", "Maho", "狐狸", "真扎", "咕噜灵波", "真布", "🦊"],
    1011: ["璃乃", "リノ", "Rino", "妹弓"],
    1012: ["初音", "ハツネ", "Hatsune", "hego", "星法", "星星法", "⭐法", "睡法", "拍大星"],
    1013: ["七七香", "ナナカ", "Nanaka", "娜娜卡", "77k", "77香", "十十力"],
    1014: ["霞", "カスミ", "Kasumi", "香澄", "侦探", "杜宾犬", "驴", "驴子", "驴妹", "🔍"],
    1015: ["美里", "ミサト", "Misato", "圣母"],
    1016: ["铃奈", "スズナ", "Suzuna", "暴击弓", "暴弓", "爆击弓", "爆弓", "辣妹弓", "政委"],
    1017: ["香织", "カオリ", "Kaori", "琉球犬", "狗子", "狗", "狗拳", "🐶", "🐕", "🐶👊🏻", "🐶👊"],
    1018: ["伊绪", "イオ", "Io", "老师", "魅魔", "依绪"],

    1020: ["美美", "ミミ", "Mimi", "兔子", "兔兔", "兔剑", "萝卜霸断剑", "人参霸断剑", "天兔霸断剑", "🐇", "🐰"],
    1021: ["胡桃", "クルミ", "Kurumi", "铃铛", "🔔"],
    1022: ["依里", "ヨリ", "Yori", "姐法", "姐姐法"],
    1023: ["绫音", "アヤネ", "Ayane", "熊锤", "🐻🔨", "🐻"],

    1025: ["铃莓", "スズメ", "Suzume", "女仆", "妹抖", "悠木碧", "umb", "雀"],
    1026: ["铃", "リン", "Rin", "松鼠", "🐿", "🐿️"],
    1027: ["惠理子", "エリコ", "Eriko", "病娇"],
    1028: ["咲恋", "サレン", "Saren", "充电宝", "青梅竹马", "幼驯染", "院长", "园长", "🔋", "普电"],
    1029: ["望", "ノゾミ", "Nozomi", "偶像", "小望", "🎤"],
    1030: ["妮诺", "ニノン", "Ninon", "妮侬", "扇子"],
    1031: ["忍", "シノブ", "Shinobu", "普忍", "鬼父", "💀"],
    1032: ["秋乃", "アキノ", "Akino", "哈哈剑"],
    1033: ["真阳", "マヒル", "Mahiru", "奶牛", "🐄", "🐮", "真☀"],
    1034: ["优花梨", "ユカリ", "Yukari", "由加莉", "黄骑", "酒鬼", "奶骑", "圣骑", "🍺", "🍺👻", "油咖喱"],

    1036: ["镜华", "キョウカ", "Kyouka", "小仓唯", "xcw", "小苍唯", "8岁", "八岁", "喷水萝", "八岁喷水萝", "8岁喷水萝"],
    1037: ["智", "トモ", "Tomo", "卜毛", "脱毛", "智爷"],
    1038: ["栞", "シオリ", "Shiori", "tp弓", "小栞", "白虎弓", "白虎妹", "栞栞", "白虎"],

    1040: ["碧", "アオイ", "Aoi", "香菜", "香菜弓", "绿毛弓", "毒弓", "绿帽弓", "绿帽"],

    1042: ["千歌", "チカ", "Chika", "绿毛奶", "精灵奶"],
    1043: ["真琴", "マコト", "Makoto", "狼", "🐺", "月月", "朋", "狼姐"],
    1044: ["伊莉亚", "イリヤ", "Iriya", "伊利亚", "伊莉雅", "伊利雅", "yly", "吸血鬼", "那个女人"],
    1045: ["空花", "クウカ", "Kuuka", "抖m", "抖"],
    1046: ["珠希", "タマキ", "Tamaki", "猫剑", "🐱剑", "🐱🗡️"],
    1047: ["纯", "ジュン", "Jun", "黑骑", "saber"],
    1048: ["美冬", "ミフユ", "Mifuyu", "子龙", "赵子龙"],
    1049: ["静流", "シズル", "Shizuru", "姐姐"],
    1050: ["美咲", "ミサキ", "Misaki", "大眼", "眼球法", "👀", "👁️", "👁"],
    1051: ["深月", "ミツキ", "Mitsuki", "眼罩", "抖s", "医生"],
    1052: ["莉玛", "リマ", "Rima", "Lima", "草泥马", "羊驼", "🦙", "🐐"],
    1053: ["莫妮卡", "モニカ", "Monika", "毛二力", "莫尼卡"],
    1054: ["纺希", "ツムギ", "Tsumugi", "裁缝", "蜘蛛侠", "🕷️", "🕸️"],
    1055: ["步未", "アユミ", "Ayumi", "步美", "路人", "路人妹"],
    1056: ["流夏", "ルカ", "Ruka", "大姐", "大姐头", "儿力", "luka", "刘夏", "露卡", "卢卡"],
    1057: ["吉塔", "ジータ", "Jiita", "姬塔", "团长", "吉他", "🎸", "骑空士", "qks"],
    1058: ["贪吃佩可", "ペコリーヌ", "Pecorine", "Pekoriinu", "佩可莉姆", "吃货", "佩可", "公主", "饭团", "🍙"],
    1059: ["可可萝", "コッコロ", "Kokkoro", "可可罗", "妈", "普白", "普妈", "kkr"],
    1060: ["凯留", "キャル", "Karyl", "Kyaru", "凯露", "百地希留耶", "希留耶", "Kiruya", "黑猫", "臭鼬", "普黑", "接头霸王", "街头霸王", "猫猫", "猫猫头"],
    1061: ["矛依未", "ムイミ", "Muimi", "诺维姆", "Noemu", "夏娜", "511", "无意义", "天楼霸断剑", "姆咪", "母咪"],

    1063: ["亚里莎", "アリサ", "Arisa", "鸭梨瞎", "瞎子", "亚里沙", "鸭梨傻", "亚丽莎", "亚莉莎", "瞎子弓", "🍐🦐", "yls"],
    1064: ["雪菲", "シェフィ", "Shephy", "Shefi", "紫布菜", "冰龙"],
    1065: ["嘉夜", "カヤ", "Kaya", "憨憨龙", "龙拳", "🐲👊🏻", "🐉👊🏻", "接龙笨比", "鬼道嘉夜", "卡雅", "卡亚", "卡娅"],
    1066: ["祈梨", "イノリ", "Inori", "梨老八", "李老八", "龙锤", "🐲🔨"],
    1067: ["帆稀", "ホマレ", "Homare", "穗希", "龙妈", "龙王", "大仓唯"],
    1068: ["拉比林斯达", "ラビリスタ", "Labyrista", "Rabirisuta", "迷宫女王", "模索路晶", "模索路", "晶", "迷宫女", "王晶", "晶姐", "日日日"],
    1069: ["真那", "マナ", "Mana", "霸瞳皇帝", "千里真那", "千里", "霸瞳", "霸铜"],
    1070: ["似似花", "ネネカ", "Neneka", "变貌大妃", "现士实似似花", "現士実似々花", "現士実", "现士实", "nnk", "448", "捏捏卡", "变貌", "大妃", "奶奶卡"],
    1071: ["克莉丝提娜", "クリスティーナ", "Kurisutiina", "誓约女君", "克莉丝提娜·摩根", "Christina", "Cristina", "克总", "女帝", "克", "摩根", "克姐"],
    1072: ["可萝爹", "長老", "Chourou", "岳父", "爷爷"],
    1073: ["拉基拉基", "ラジニカーント", "Rajinigaanto", "跳跃王", "Rajiraji", "Lajilaji", "垃圾垃圾", "教授"],

    1075: ["贪吃佩可(夏日)", "ペコリーヌ(サマー)", "Pecorine(Summer)", "Pekoriinu(Summer)", "佩可莉姆(夏日)", "水吃", "水饭", "水吃货", "水佩可", "水公主", "水饭团", "水🍙", "泳吃", "泳饭", "泳吃货", "泳佩可", "泳公主", "泳饭团", "泳🍙", "泳装吃货", "泳装公主", "泳装饭团", "泳装🍙", "佩可(夏日)", "🥡", "👙🍙", "泼妇"],
    1076: ["可可萝(夏日)", "コッコロ(サマー)", "Kokkoro(Summer)", "水白", "水妈", "水可", "水可可", "水可可萝", "水可可罗", "泳装妈", "泳装可可萝", "泳装可可罗"],
    1077: ["铃莓(夏日)", "スズメ(サマー)", "Suzume(Summer)", "水女仆", "水妹抖"],
    1078: ["凯留(夏日)", "キャル(サマー)", "Karyl(Summer)", "Kyaru(Summer)", "凯露(夏日)", "水黑", "水黑猫", "水臭鼬", "泳装黑猫", "泳装臭鼬", "潶", "溴", "💧黑", "流泪猫猫头"],
    1079: ["珠希(夏日)", "タマキ(サマー)", "Tamaki(Summer)", "水猫剑", "水猫", "渵", "💧🐱", "💧🐱🗡️", "水🐱🗡️"],
    1080: ["美冬(夏日)", "ミフユ(サマー)", "Mifuyu(Summer)", "水子龙", "水美冬"],
    1081: ["忍(万圣节)", "シノブ(ハロウィン)", "Shinobu(Halloween)", "万圣忍", "瓜忍", "鬼忍", "🎃忍", "🎃💀"],
    1082: ["宫子(万圣节)", "ミヤコ(ハロウィン)", "Miyako(Halloween)", "万圣宫子", "万圣布丁", "狼丁", "狼布丁", "万圣🍮", "🐺🍮", "🎃🍮", "👻🍮"],
    1083: ["美咲(万圣节)", "ミサキ(ハロウィン)", "Misaki(Halloween)", "万圣美咲", "万圣大眼", "瓜眼", "🎃眼", "🎃👀", "🎃👁️", "🎃👁"],
    1084: ["千歌(圣诞节)", "チカ(クリスマス)", "Chika(Xmas)", "圣诞千歌", "圣千", "蛋鸽", "🎄💰🎶", "🎄千🎶", "🎄1000🎶"],
    1085: ["胡桃(圣诞节)", "クルミ(クリスマス)", "Kurumi(Xmas)", "圣诞胡桃", "圣诞铃铛"],
    1086: ["绫音(圣诞节)", "アヤネ(クリスマス)", "Ayane(Xmas)", "圣诞熊锤", "蛋锤", "圣锤", "🎄🐻🔨", "🎄🐻"],
    1087: ["日和(新年)", "ヒヨリ(ニューイヤー)", "Hiyori(NewYear)", "新年日和", "春猫", "👘🐱"],
    1088: ["优衣(新年)", "ユイ(ニューイヤー)", "Yui(NewYear)", "新年优衣", "春田", "新年由衣"],
    1089: ["怜(新年)", "レイ(ニューイヤー)", "Rei(NewYear)", "春剑", "春怜", "春伶", "新春剑圣", "新年怜", "新年剑圣"],
    1090: ["惠理子(情人节)", "エリコ(バレンタイン)", "Eriko(Valentine)", "情人节病娇", "恋病", "情病", "恋病娇", "情病娇", "青椒"],
    1091: ["静流(情人节)", "シズル(バレンタイン)", "Shizuru(Valentine)", "情人节静流", "情姐", "情人节姐姐", "恋姐"],
    1092: ["安", "アン", "An", "胖安", "55kg", "小安"],
    1093: ["露", "ルゥ", "Ruu", "逃课女王", "补考女帝"],
    1094: ["古蕾娅", "グレア", "Gurea", "龙姬", "古雷娅", "古蕾亚", "古雷亚", "古蕾雅", "🐲🐔", "🐉🐔"],
    1095: ["空花(大江户)", "クウカ(オーエド)", "Kuuka(Ooedo)", "江户空花", "江户抖m", "江m", "花m", "江花", "大江m", "花抖"],
    1096: ["妮诺(大江户)", "ニノン(オーエド)", "Ninon(Ooedo)", "江户扇子", "忍扇"],
    1097: ["雷姆", "レム", "Remu", "蕾姆"],
    1098: ["拉姆", "ラム", "Ramu"],
    1099: ["爱蜜莉雅", "エミリア", "Emiria", "艾米莉亚", "emt"],
    1100: ["铃奈(夏日)", "スズナ(サマー)", "Suzuna(Summer)", "瀑击弓", "水爆", "水爆弓", "水暴", "瀑", "水暴弓", "水暴击弓", "水政委", "瀑弓", "泳装暴弓", "泳装爆弓", "泳装政委"],
    1101: ["伊绪(夏日)", "イオ(サマー)", "Io(Summer)", "水魅魔", "水老师", "泳装魅魔", "泳装老师", "水io"],
    1102: ["美咲(夏日)", "ミサキ(サマー)", "Misaki(Summer)", "水美咲", "水大眼", "泳装大眼"],
    1103: ["咲恋(夏日)", "サレン(サマー)", "Saren(Summer)", "水电", "泳装充电宝", "泳装咲恋", "水着咲恋", "水电站", "水电宝", "水充", "👙🔋"],
    1104: ["真琴(夏日)", "マコト(サマー)", "Makoto(Summer)", "水狼", "浪", "水🐺", "泳狼", "泳月", "泳月月", "泳朋", "水月", "水月月", "水朋", "👙🐺"],
    1105: ["香织(夏日)", "カオリ(サマー)", "Kaori(Summer)", "水狗", "泃", "水🐶", "水🐕", "泳狗", "水狗拳"],
    1106: ["真步(夏日)", "マホ(サマー)", "Maho(Summer)", "水狐狸", "水狐", "水壶", "水真步", "水maho", "氵🦊", "水🦊", "💧🦊"],
    1107: ["碧(插班生)", "アオイ(編入生)", "Aoi(Hennyuusei)", "生菜", "插班碧", "学院碧", "转校弓", "转学弓"],
    1108: ["克萝依", "クロエ", "Kuroe", "克罗依", "华哥", "黑江", "黑江花子", "花子"],
    1109: ["琪爱儿", "チエル", "Chieru", "千爱瑠", "切露", "茄露", "茄噜", "切噜", "佐仓"],
    1110: ["优妮", "ユニ", "Yuni", "真行寺由仁", "由仁", "优尼", "u2", "优妮辈先", "辈先", "书记", "uni", "先辈", "仙贝", "油腻", "优妮先辈", "学姐", "18岁黑丝学姐", "咖啡人"],
    1111: ["镜华(万圣节)", "キョウカ(ハロウィン)", "Kyouka(Halloween)", "万圣镜华", "万圣小仓唯", "万圣xcw", "猫仓唯", "黑猫仓唯", "mcw", "猫唯", "猫仓", "喵唯"],
    1112: ["禊(万圣节)", "ミソギ(ハロウィン)", "Misogi(Halloween)", "万圣禊", "万圣炸弹人", "瓜炸弹人", "万圣炸弹", "万圣炸", "瓜炸", "南瓜炸", "万圣节禊", "万圣熊孩", "🎃💣"],
    1113: ["美美(万圣节)", "ミミ(ハロウィン)", "Mimi(Halloween)", "万圣兔", "万圣兔子", "万圣兔兔", "绷带兔", "绷带兔子", "万圣美美", "绷带美美", "瓜兔", "万圣🐰", "绷带🐰", "🎃🐰", "万圣🐇", "绷带🐇", "🎃🐇"],
    1114: ["露娜", "ルナ", "Runa", "Luna", "露仓唯", "露cw"],
    1115: ["克莉丝提娜(圣诞节)", "クリスティーナ(クリスマス)", "Kurisutiina(Xmas)", "Christina(Xmas)", "Cristina(Xmas)", "圣诞克", "圣诞克总", "圣诞女帝", "蛋克", "蛋壳", "圣克", "必胜客"],
    1116: ["望(圣诞节)", "ノゾミ(クリスマス)", "Nozomi(Xmas)", "圣诞望", "圣诞偶像", "蛋偶像", "蛋望"],
    1117: ["伊莉亚(圣诞节)", "イリヤ(クリスマス)", "Iriya(Xmas)", "圣诞伊莉亚", "圣诞伊利亚", "圣诞伊莉雅", "圣诞伊利雅", "圣诞yly", "圣诞吸血鬼", "圣伊", "圣yly", "伊利丹"],
    1118: ["贪吃佩可(新年)", "ペコリーヌ(ニューイヤー)", "Pecorine(NewYear)", "佩可莉姆(新年)", "春吃", "新吃", "新年吃货", "年货"],
    1119: ["可可萝(新年)", "コッコロ(ニューイヤー)", "Kokkoro(NewYear)", "春可可", "春白", "新年妈", "春妈"],
    1120: ["凯留(新年)", "キャル(ニューイヤー)", "Karyl(NewYear)", "Kyaru(NewYear)", "凯露(新年)", "春凯留", "春黑猫", "春黑", "春臭鼬", "新年凯留", "新年黑猫", "新年臭鼬", "唯一神", "神"],
    1121: ["铃莓(新年)", "スズメ(ニューイヤー)", "Suzume(NewYear)", "春铃莓", "春女仆", "春妹抖", "新年铃莓", "新年女仆", "新年妹抖"],
    1122: ["霞(魔法少女)", "カスミ(マジカル)", "Kasumi(MagiGirl)", "魔法少女霞", "魔法侦探", "魔法杜宾犬", "魔法驴", "魔法驴子", "魔驴", "魔法霞", "魔法少驴"],
    1123: ["栞(魔法少女)", "シオリ(マジカル)", "Shiori(MagiGirl)", "魔法少女栞", "魔法tp弓", "魔法小栞", "魔法白虎弓", "魔法白虎妹", "魔法白虎", "魔栞", "魔弓", "魔法弓", "法弓"],
    1124: ["卯月(NGs)", "ウヅキ(デレマス)", "Udsuki(DEREM@S)", "卯月(偶像大师)", "卯月", "卵用", "Udsuki(DEREMAS)", "岛村卯月", "Udsuki"],
    1125: ["凛(NGs)", "リン(デレマス)", "Rin(DEREM@S)", "凛(偶像大师)", "凛", "Rin(DEREMAS)", "涩谷凛", "西部凛"],
    1126: ["未央(NGs)", "ミオ(デレマス)", "Mio(DEREM@S)", "未央(偶像大师)", "未央", "Mio(DEREMAS)", "本田未央", "Mio"],
    1127: ["铃(游侠)", "リン(レンジャー)", "Rin(Ranger)", "骑兵松鼠", "游侠松鼠", "游骑兵松鼠", "护林员松鼠", "护林松鼠", "游侠🐿️", "武松", "钻头松鼠"],
    1128: ["真阳(游侠)", "マヒル(レンジャー)", "Mahiru(Ranger)", "骑兵奶牛", "游侠奶牛", "游骑兵奶牛", "护林员奶牛", "护林奶牛", "游侠🐄", "游侠🐮", "牛叉"],
    1129: ["璃乃(奇幻)", "リノ(ワンダー)", "Rino(Wonder)", "璃乃(奇境)", "璃乃(仙境)", "爽弓", "爱丽丝弓", "爱弓", "兔弓", "奇境妹弓", "奇幻妹弓", "奇幻璃乃", "仙境妹弓", "白丝妹弓", "爱丽丝妹弓"],
    1130: ["步未(奇幻)", "アユミ(ワンダー)", "Ayumi(Wonder)", "步未(奇境)", "步未(仙境)", "路人兔", "兔人妹", "爱丽丝路人", "奇境路人", "奇幻路人", "奇幻步未", "仙境路人", "爱丽丝路人妹", "梦路"],
    1131: ["流夏(夏日)", "ルカ(サマー)", "Ruka(Summer)", "泳装流夏", "水流夏", "泳装刘夏", "水刘夏", "泳装大姐", "泳装大姐头", "水大姐", "水大姐头", "水儿力", "泳装儿力", "水流"],
    1132: ["杏奈(夏日)", "アンナ(サマー)", "Anna(Summer)", "泳装中二", "泳装煤气罐", "水中二", "水煤气罐", "冲", "冲二"],
    1133: ["七七香(夏日)", "ナナカ(サマー)", "Nanaka(Summer)", "泳装娜娜卡", "泳装77k", "泳装77香", "水娜娜卡", "水77k", "水77香", "水七七香", "泳装七七香", "水七"],
    1134: ["初音(夏日)", "ハツネ(サマー)", "Hatsune(Summer)", "水星", "海星", "水hego", "水星法", "泳装星法", "水⭐法", "水睡法", "湦", "泳装初音", "水初音", "夏日初音"],
    1135: ["美里(夏日)", "ミサト(サマー)", "Misato(Summer)", "水母", "泳装圣母", "水圣母"],
    1136: ["纯(夏日)", "ジュン(サマー)", "Jun(Summer)", "泳装黑骑", "水黑骑", "泳装纯", "水纯", "小次郎"],
    1137: ["茜里(天使)", "アカリ(エンジェル)", "Akari(Angel)", "天使妹法", "天使茜里", "丘比特妹法", "天妹"],
    1138: ["依里(天使)", "ヨリ(エンジェル)", "Yori(Angel)", "天使姐法", "天使依里", "丘比特姐法", "天姐"],
    1139: ["纺希(万圣节)", "ツムギ(ハロウィン)", "Tsumugi(Halloween)", "万圣裁缝", "万圣蜘蛛侠", "🎃🕷️", "🎃🕸️", "万裁", "瓜裁", "鬼裁", "鬼才"],
    1140: ["怜(万圣节)", "レイ(ハロウィン)", "Rei(Halloween)", "万圣剑圣", "万剑", "瓜剑", "瓜怜", "万圣怜", "鬼剑", "鬼怜"],
    1141: ["茉莉(万圣节)", "マツリ(ハロウィン)", "Matsuri(Halloween)", "万圣跳跳虎", "万圣老虎", "瓜虎", "万圣虎", "🎃🐅"],
    1142: ["莫妮卡(魔法少女)", "モニカ(マジカル)", "Monika(MagiGirl)", "魔法少女莫妮卡", "魔二力", "魔卡少女"],
    1143: ["智(魔法少女)", "トモ(マジカル)", "Tomo(MagiGirl)", "魔法少女智", "琪露诺", "9智", "⑨"],
    1144: ["秋乃(圣诞节)", "アキノ(クリスマス)", "Akino(Xmas)", "圣剑", "生煎", "圣诞哈哈剑", "哈哈剑(圣诞节)", "圣哈", "蛋哈", "蛋剑"],
    1145: ["咲恋(圣诞节)", "サレン(クリスマス)", "Saren(Xmas)", "圣诞充电宝", "圣电", "圣诞咲恋"],
    1146: ["优花梨(圣诞节)", "ユカリ(クリスマス)", "Yukari(Xmas)", "蛋黄", "由加莉(圣诞节)", "圣诞黄骑", "圣诞圣骑", "蛋骑", "黄骑(圣诞节)", "圣黄"],
    1147: ["矛依未(新年)", "ムイミ(ニューイヤー)", "Muimi(NewYear)", "新年511", "春511", "春11", "春矛", "512"],


    1150: ["似似花(新年)", "ネネカ(ニューイヤー)", "Neneka(NewYear)", "新年似似花", "春似似花", "春nnk", "春花", "新年nnk", "春妃", "春448"],




    1155: ["可可萝(祭服)", "コッコロ(儀装束)", "Kokkoro(Costume)", "可可萝(仪装束)", "礼妈", "仪妈", "仪装妈", "姨妈", "礼白"],
    1156: ["优衣(祭服)", "ユイ(儀装束)", "Yui(Costume)", "优衣(仪装束)", "礼ue", "礼装ue", "礼装优衣", "仪装ue", "礼衣", "礼田"],
    1157: ["霞(夏日)", "カスミ(サマー)", "Kasumi(Summer)", "水驴", "泳装驴", "沪"],
    1158: ["莉玛(灰姑娘)", "リマ(シンデレラ)", "Rima(Cinderella)", "人形羊驼", "人驼", "灰驼", "灰姑娘羊驼", "灰羊"],
    1159: ["真琴(灰姑娘)", "マコト(シンデレラ)", "Makoto(Cinderella)", "灰姑娘狼", "灰狼"],
    1160: ["真步(灰姑娘)", "マホ(シンデレラ)", "Maho(Cinderella)", "灰姑娘狐狸", "灰狐狸", "灰狐", "灰壶", "茶狐", "茶壶"],

    1162: ["克萝依(圣学祭)", "クロエ(聖学祭)", "Kuroe(Seigakusai)", "运动华", "运动华哥", "圣学祭华", "圣学祭克萝依", "圣华"],
    1163: ["琪爱儿(圣学祭)", "チエル(聖学祭)", "Chieru(Seigakusai)", "千爱瑠(圣学祭)", "运动切噜", "圣学祭切噜", "圣学祭琪爱儿", "圣学祭千爱瑠", "圣爱瑠"],
    1164: ["优妮(圣学祭)", "ユニ(聖学祭)", "Yuni(Seigakusai)", "圣优妮", "圣uni", "运动优妮", "运动服", "罗塞塔"],
    1165: ["祈梨(时间旅行)", "イノリ(タイムトラベル)", "Inori(TimeTravel)", "时间旅行龙锤", "穿越龙锤", "穿越梨老八", "军装龙锤", "元首龙锤", "元首", "元老八"],
    1166: ["嘉夜(时间旅行)", "カヤ(タイムトラベル)", "Kaya(TimeTravel)", "时间旅行龙拳", "穿越龙拳", "水手龙", "水手龙拳", "时空龙拳"],
    1167: ["碧(作业服)", "アオイ(作業服)", "Aoi(Sagyoufuku)", "碧(工作服)", "工菜", "韭菜", "工作碧", "贡菜"],
    1168: ["珠希(作业服)", "タマキ(作業服)", "Tamaki(Sagyoufuku)", "珠希(工作服)", "工猫贼", "工猫剑", "工贼", "工珠希"],
    1169: ["美冬(作业服)", "ミフユ(作業服)", "Mifuyu(Sagyoufuku)", "美冬(工作服)", "电子龙", "工子龙", "工龙", "工头"],
    1170: ["惠理子(夏日)", "エリコ(サマー)", "Eriko(Summer)", "泳装惠理子", "泳装病娇", "水病", "水病娇", "水饺", "水娇"],
    1171: ["静流(夏日)", "シズル(サマー)", "Shizuru(Summer)", "泳装静流", "泳装姐姐", "水姐", "水姐姐", "水解", "沮"],
    1172: ["望(夏日)", "ノゾミ(サマー)", "Nozomi(Summer)", "泳装偶像", "泳装望", "水望", "水偶像", "夏日偶像", "夏日望", "潒"],
    1173: ["千歌(夏日)", "チカ(サマー)", "Chika(Summer)", "泳装千歌", "水千", "汘", "泳千"],
    1174: ["纺希(夏日)", "ツムギ(サマー)", "Tsumugi(Summer)", "泳装裁缝", "泳装纺希", "水裁缝", "水裁", "水彩", "水纺希", "漨"],
    1175: ["深月(大江户)", "ミツキ(オーエド)", "Mitsuki(Ooedo)", "江月", "江S", "江户深月", "大江户深月"],
    1176: ["雪(大江户)", "ユキ(オーエド)", "Yuki(Ooedo)", "江雪", "江哥", "江户雪", "江户小雪", "江户雪哥", "大江户雪"],
    1177: ["香织(万圣节)", "カオリ(ハロウィン)", "Kaori(Halloween)", "万圣狗", "瓜狗", "万圣狗拳"],
    1178: ["妮诺(万圣节)", "ニノン(ハロウィン)", "Ninon(Halloween)", "万圣扇", "瓜扇", "万圣扇子"],
    1179: ["铃奈(万圣节)", "スズナ(ハロウィン)", "Suzuna(Halloween)", "万圣暴弓", "瓜弓", "瓜暴弓", "万圣爆弓", "瓜爆弓"],
    1180: ["克蕾琪塔", "クレジッタ", "Kurejitta", "富婆", "信用卡"],
    1181: ["兰法", "ランファ", "Ranfa", "Ranpha", "兰法妈妈", "兰妈妈", "兰妈"],
    1182: ["美空", "ミソラ", "Misora", "坏女人", "魅空", "流魅空", "流美空"],
    1183: ["初音(初音&栞)", "ハツネ(ハツネ&シオリ)", "Hatsune(Hatsune&Shiori)", "星弓星", "星栞星"],
    1184: ["栞(初音&栞)", "シオリ(ハツネ&シオリ)", "Shiori(Hatsune&Shiori)", "星弓栞", "星弓弓", "星栞栞", "星栞弓"],
    1185: ["花凛", "カリン", "Karin", "佳凛", "绿色恶魔", "绿魔", "绿毛恶魔"],




    1190: ["伊绪(黑暗)", "イオ(ノワール)", "Io(Noir)", "黑老师", "黑魅魔"],
    1191: ["空花(黑暗)", "クウカ(ノワール)", "Kuuka(Noir)", "黑m", "暗m"],
    1192: ["真阳(圣诞节)", "マヒル(クリスマス)", "Mahiru(Xmas)", "圣牛", "蛋牛", "圣诞奶牛", "圣诞牛"],
    1193: ["璃乃(圣诞节)", "リノ(クリスマス)", "Rino(Xmas)", "圣诞妹弓", "圣诞璃乃", "弹弓", "蛋弓", "诞弓"],





    1199: ["宫子(圣诞节)", "ミヤコ(クリスマス)", "Miyako(Xmas)", "圣诞布丁", "圣诞宫子", "诞丁", "蛋丁", "但丁"],
    1200: ["静流(黑暗)", "シズル(ノワール)", "黑姐姐", "黑姐"],




    1204: ["美美(小小甜心)", "ミミ(リトルリリカル)", "Mimi(LittleLyrical)"],
    1205: ["禊(小小甜心)", "ミソギ(リトルリリカル)", "Misogi(LittleLyrical)", "未奏希(小小甜心)"],
    1206: ["镜华(小小甜心)", "キョウカ(リトルリリカル)", "Kyouka(LittleLyrical)"],
    1207: ["雪菲(新年)", "シェフィ(ニューイヤー)", "Shephy(NewYear)", "Shefi(NewYear)", "新年雪菲", "春雪菲", "春菲", "春冰龙"],
    1208: ["流夏(新年)", "ルカ(ニューイヤー)", "Ruka(NewYear)", "春流夏", "春流"],
    1209: ["伊莉亚(新年)", "イリヤ(ニューイヤー)", "Iriya(NewYear)", "新年伊莉亚", "新年伊利亚", "新年伊莉雅", "新年伊利雅", "新年yly", "新年吸血鬼", "春伊", "春yly", "伊莉旦"],
    1210: ["贪吃佩可(超载)", "ペコリーヌ(オーバーロード)", "Pecorine(Overload)", "Pekoriinu(Overload)", "超载吃", "超吃", "超载佩可", "超载佩", "超佩"],
    1211: ["凯留(超载)", "キャル(オーバーロード)", "Karyl(Overload)", "凯露(超载)", "Kyaru(Overload)", "超载凯留", "超凯留", "超载黑猫", "超黑", "超猫", "超威蓝猫"],
    1212: ["拉比林斯达(超载)", "ラビリスタ(オーバーロード)", "Labyrista(Overload)", "Rabirisuta(Overload)", "超载晶", "超晶"],
    1213: ["胡桃(舞台)", "クルミ(ステージ)", "Kurumi(Stage)", "舞台胡桃", "舞桃", "演员", "舞胡", "芜湖", "舞铃", "舞台铃", "戏铃"],
    1214: ["美咲(舞台)", "ミサキ(ステージ)", "Misaki(Satge)", "舞台大眼", "舞台眼", "舞台美咲", "泥头车大眼", "车眼"],
    1215: ["步未(怪盗)", "アユミ(怪盗)", "Ayumi(Kaitou)", "怪盗路人", "怪盗路人妹"],
    1216: ["祈梨(怪盗)", "イノリ(怪盗)", "Inori(Kaitou)", "怪盗祈梨", "怪盗龙锤", "忍龙", "忍龙锤"],
    1217: ["秋乃(秋乃&咲恋)", "アキノ(アキノ&サレン)", "Akino(Akino&Saren)"],
    1218: ["咲恋(秋乃&咲恋)", "サレン(アキノ&サレン)", "Saren(Akino&Saren)"],
    1219: ["杏奈(海盗)", "アンナ(パイレーツ)", "Anna(Pirates)", "海盗中二", "海盗杏奈", "船长中二", "船二"],
    1220: ["忍(海盗)", "シノブ(パイレーツ)", "Shinobu(Pirates)", "海盗忍", "海贼忍", "海忍", "水手忍", "手忍"],
    1221: ["碧(露营)", "アオイ(キャンプ)", "Aoi(Camp)", "露营碧", "露碧", "野菜"],
    1222: ["优花梨(露营)", "ユカリ(キャンプ)", "Yukari(Camp)", "露营优花梨", "露优花梨", "露花梨", "露营黄骑", "露黄骑", "露黄"],
    1223: ["斑比", "ヴァンピィ", "Vampy", "Vania", "斑比酱", "钉宫"],
    1224: ["日和(夏日)", "ヒヨリ(サマー)", "Hiyori(Summer)", "水猫拳", "水日和"],
    1225: ["怜(夏日)", "レイ(サマー)", "Rei(Summer)", "水怜", "水剑圣"],
    1226: ["优衣(夏日)", "ユイ(サマー)", "Yui(Summer)", "水优衣", "水ue", "水田", "泳衣", "游依", "水草"],
    1227: ["镜华(夏日)", "キョウカ(サマー)", "Kyouka(Summer)", "泳装镜华", "水镜华", "水xcw", "水仓唯", "水cw", "scw"],
    1228: ["禊(夏日)", "ミソギ(サマー)", "Misogi(Summer)", "未奏希(夏日)", "水禊", "水炸弹人", "水炸", "水未奏希", "泳装炸弹人", "泳装未奏希"],
    1229: ["美美(夏日)", "ミミ(サマー)", "Mimi(Summer)", "水美美", "泳装美美", "水兔", "水兔兔", "水兔子"],
    1230: ["爱梅斯", "アメス", "Amesu", "菲欧", "爱美斯", "艾美斯", "艾梅斯"],
    1231: ["真步(探险家)",  "マホ(エクスプローラー)", "野狐", "探狐", "尻狐", "屁狐", "屁胡"],   
    1232: ["绫音(探险家)", "アヤネ(エクスプローラー)", "野锤", "野炊"],   
    1233: ["涅娅", "ネア", "小黄", "史莱姆", "黄史莱姆"],   

    1235: ["铃(万圣节)", "リン(ハロウィン)", "瓜松鼠", "鬼松鼠", "万圣松鼠"],   
    1236: ["智(万圣节)", "トモ(ハロウィン)", "瓜智", "鬼智", "万圣智"],   
    1237: ["七七香(万圣节)", "ナナカ(ハロウィン)", "鬼七", "瓜七", "万圣七七香", "鬼泣"],     
    1238: ["克莉丝提娜(野性)", "クリスティーナ(ワイルド)", "兔克", "兔女郎克", "野克"],     
    1239: ["茉莉(野性)", "マツリ(ワイルド)", "小虎", "野老虎"],    
    1240: ["茜里(圣诞节)", "アカリ(クリスマス)", "圣妹", "圣诞妹法"],    
    1241: ["依里(圣诞节)", "ヨリ(クリスマス)", "圣姐", "圣诞姐法"],   
    1242: ["纯(圣诞节)", "ジュン(クリスマス)", "圣骑", "白骑", "圣黑骑", "圣诞黑骑"],
    1245: ["帆稀(新年)", "ホマレ(ニューイヤー)", "春龙妈", "新年龙妈"],
    1246: ["美里(新年)", "ミサト(ニューイヤー)", "春母", "新母", "新年圣母"],
    1247: ["深月(新年)", "ミツキ(ニューイヤー)", "春月", "新月", "新年深月"],



    1251: ["珠希(咖啡馆)", "タマキ(カフェ)", "猫咖", "咖啡猫"],
    1252: ["莫妮卡(咖啡馆)", "モニカ(カフェ)", "莫妮咖"],

    # =================================== #
    1701: ["环奈", "カンナ", "Kanna", "桥本环奈", "红二力", "毛大力", "毛小力", "毛六力", "可大萝", "大可萝", "缝合怪", "一环"],
    1702: ["环奈(振袖)", "カンナ(振袖)", "Kanna(Furisode)", "振袖环奈", "春环", "春奈", "春环奈", "二环", "振环奈", "振环", "甄嬛", "震动环", "年糕环奈", "年糕环"],







    # =================================== #
    1801: ["日和(公主)", "ヒヨリ(プリンセス)", "Hiyori(Princess)", "公主日和", "公猫", "炎拳猫", "火猫", "炎拳"],
    1802: ["优衣(公主)", "ユイ(プリンセス)", "Yui(Princess)", "公主优衣", "公主yui", "公主种田", "公主田", "公主ue", "掉毛优衣", "掉毛yui", "掉毛ue", "掉毛", "飞翼优衣", "飞翼ue", "飞翼", "飞翼高达", "飞田", "羽田", "羽衣", "毛衣", "pfue"],
    1803: ["怜(公主)", "レイ(プリンセス)", "Rei(Princess)", "公主怜", "公剑", "风剑", "pf怜"],
    1804: ["贪吃佩可(公主)", "ペコリーヌ(プリンセス)", "Pecorine(Princess)", "佩可莉姆(公主)", "Pekoriinu(Princess)", "公主吃", "公主饭", "公主吃货", "公主佩可", "公主饭团", "公主🍙", "命运高达", "高达", "命运公主", "高达公主", "命吃", "春哥高达", "🤖🍙", "🤖", "公吃", "pf吃"],
    1805: ["可可萝(公主)", "コッコロ(プリンセス)", "Kokkoro(Princess)", "公主妈", "月光妈", "蝶妈", "蝴蝶妈", "月光蝶妈", "公主可", "公主可萝", "公主可可萝", "月光可", "月光可萝", "月光可可萝", "蝶可", "蝶可萝", "蝶可可萝", "公可", "pf妈", "飞妈"],
    1806: ["凯留(公主)", "キャル(プリンセス)", "Karyl(Princess)", "Kyaru(Princess)", "凯露(公主)", "公主黑猫", "公主猫", "公主猫猫头", "白猫"],
    1807: ["初音&栞", "ハツネ&シオリ", "Hatsune&Shiori", "星弓", "星栞", "双子弓", "姐妹弓", "姊妹弓", "姐妹丼", "姊妹丼", "姐妹井", "贴贴弓", "替身弓", "白金之星", "食堂泼辣酱", "初音栞", "星法栞"],
    1808: ["禊&美美&镜华", "ミソギ&ミミ&キョウカ", "Misogi&Mimi&Kyouka", "小小甜心", "狱三家", "小御三家"],
    1809: ["秋乃&咲恋", "アキノ&サレン", "Akino&Saren", "咲哈哈", "哈哈电", "哈哈咲", "哈电", "电哈", "光焰"],
    1810: ["安&古蕾雅", "アン＆グレア", "双姬", "古安"],








    # =================================== #
    # 1900: ["爱梅斯", "アメス", "Amesu"],
    1901: ["菲欧", "フィオ", "Fio"],





    1907: ["大古", "タイゴ", "Taigo", "大吾", "鬼道大吾"],
    # 1908: ["花凛", "カリン", "Karin", "绿毛恶魔"],
    1909: ["涅比亚", "ネビア", "Nevia", "Nebia"],
    1910: ["真崎", "マサキ", "Masaki"],
    1911: ["米涅尔β", "ミネルβ", "MineruBeta", "米涅尔", "ミネル", "Mineru"],

    1913: ["和正", "カズマサ", "Kazumasa"],
    1914: ["豪绅", "ゴウシン", "Goushin"],
    # 1915: ["克蕾琪塔", "クレジッタ", "Kurejitta"],
    1916: ["基洛", "キイロ", "Kiiro"],
    1917: ["赞恩", "ゼーン", "Seen", "大舅哥", "Zane"],
    # 1918: ["兰法", "ランファ", "Ranfa", "Ranpha"],
    1919: ["阿佐尔德", "アンゾールド", "Anzoorudo", "猪哥", "Azold"],
    # 1920: ["美空", "ミソラ", "Misora"],









    # =================================== #
    4031: ["骷髅", "髑髏", "Dokuro", "骷髅老爹", "老爹"],

    9000: ["祐树", "ユウキ", "Yuuki", "骑士", "骑士君"],
}

CHARA_PROFILE = {
    1001: {"名字": "日和", "公会": "破晓之星", "生日": "8月27日", "年龄": "16", "身高": "155cm", "体重": "44kg", "血型": "A", "种族": "兽人族", "喜好": "助人、打气加油", "声优": "东山奈央", "口头禅和座右铭": "放不下心"},
    1002: {"名字": "优衣", "公会": "破晓之星", "生日": "4月5日", "年龄": "17", "身高": "158cm", "体重": "47kg", "血型": "O", "种族": "人族", "喜好": "料理、观察人类", "声优": "种田梨沙", "特技": "全体治愈", "儿时玩伴": "真琴"},
    1003: {"名字": "怜", "公会": "破晓之星", "生日": "1月12日", "年龄": "18", "身高": "163cm", "体重": "46kg", "血型": "B", "种族": "魔族", "喜好": "读书、骑马、茶", "声优": "早见沙织", "隐藏特技": "骑马"},
    1004: {"名字": "禊", "公会": "小小甜心", "生日": "8月10日", "年龄": "9", "身高": "128cm", "体重": "27kg", "血型": "O", "种族": "人族", "喜好": "恶作剧、探险", "声优": "诸星堇", "无人能出其右的技巧": "捣蛋鬼"},
    1005: {"名字": "茉莉", "公会": "王宫骑士团", "生日": "11月25日", "年龄": "12", "身高": "146cm", "体重": "40kg", "血型": "O", "种族": "兽人族", "喜好": "英雄扮演游戏", "声优": "下田麻美", "称号": "见习英雄"},
    1006: {"名字": "茜里", "公会": "恶魔伪王国军", "生日": "11月22日", "年龄": "13", "身高": "150cm", "体重": "42kg", "血型": "O", "种族": "魔族", "喜好": "萨克斯风", "声优": "浅仓杏美", "称号": "小恶魔", "姊姊": "依里"},
    1007: {"名字": "宫子", "公会": "恶魔伪王国军", "生日": "1月23日", "年龄": "14", "身高": "130cm", "体重": "32kg", "血型": "B", "种族": "魔族", "喜好": "吃布丁", "声优": "雨宫天"},
    1008: {"名字": "雪", "公会": "纯白之翼兰德索尔分部", "生日": "10月10日", "年龄": "14", "身高": "150cm", "体重": "40kg", "血型": "AB", "种族": "精灵族", "喜好": "欣赏镜中的自己", "声优": "大空直美", "罪过": "美丽的自己", "癖好": "自恋"},
    1009: {"名字": "杏奈", "公会": "暮光流星群", "生日": "7月5日", "年龄": "17", "身高": "159cm", "体重": "45kg", "血型": "A", "种族": "魔族", "喜好": "写小说", "声优": "高野麻美", "称号": "疾风之冥姬"},
    1010: {"名字": "真步", "公会": "自卫团", "生日": "9月22日", "年龄": "16", "身高": "155cm", "体重": "42kg", "血型": "O", "种族": "兽人族", "喜好": "幻想、收集玩偶", "声优": "内田真礼", "身份": "某谜之国度的公主"},
    1011: {"名字": "璃乃", "公会": "拉比林斯", "生日": "8月25日", "年龄": "15", "身高": "156cm", "体重": "44kg", "血型": "A", "种族": "人族", "喜好": "裁缝", "声优": "阿澄佳奈", "自称": "妹妹", "称号": "小笨蛋"},
    1012: {"名字": "初音", "公会": "森林守卫", "生日": "12月24日", "年龄": "17", "身高": "156cm", "体重": "46kg", "血型": "A", "种族": "精灵族", "喜好": "和妹妹一起玩、回笼觉、午睡、早睡", "声优": "大桥彩香", "称号": "超能力少女", "妹妹": "小栞"},
    1013: {"名字": "七七香", "公会": "暮光流星群", "生日": "8月21日", "年龄": "18", "身高": "166cm", "体重": "55kg", "血型": "O", "种族": "魔族", "喜好": "读书、魔法", "声优": "佳村遥", "称号": "魔法少女"},
    1014: {"名字": "霞", "公会": "自卫团", "生日": "11月3日", "年龄": "15", "身高": "152cm", "体重": "41kg", "血型": "AB", "种族": "兽人族", "喜好": "读书、推理", "声优": "水濑祈", "称号": "名侦探"},
    1015: {"名字": "美里", "公会": "森林守卫", "生日": "9月5日", "年龄": "21", "身高": "165cm", "体重": "54kg", "血型": "O", "种族": "精灵族", "喜好": "制作绘本", "声优": "国府田麻理子", "工作": "幼稚园的老师"},
    1016: {"名字": "铃奈", "公会": "月光学院", "生日": "4月10日", "年龄": "18", "身高": "167cm", "体重": "48kg", "血型": "O", "种族": "魔族", "喜好": "时尚", "声优": "上坂堇", "工作": "超级名模", "称号": "辣妹"},
    1017: {"名字": "香织", "公会": "自卫团", "生日": "7月7日", "年龄": "19", "身高": "158cm", "体重": "53kg", "血型": "A", "种族": "兽人族", "喜好": "跳舞、空手道", "声优": "高森奈津美", "绝技": "琉球空手道", "问候的方式": "嗨——呵"},
    1018: {"名字": "伊绪", "公会": "月光学院", "生日": "8月14日", "年龄": "23", "身高": "162cm", "体重": "52kg", "血型": "B", "种族": "魔族", "喜好": "看恋爱小说、恋爱剧、恋爱漫画", "声优": "伊藤静", "工作": "新来的老师"},
    1020: {"名字": "美美", "公会": "小小甜心", "生日": "4月3日", "年龄": "10", "身高": "117cm", "体重": "21kg", "血型": "O", "种族": "兽人族", "喜好": "收集可爱的东西", "声优": "日高里菜", "最喜欢": "兔子先生"},
    1021: {"名字": "胡桃", "公会": "咲恋救济院", "生日": "6月9日", "年龄": "12", "身高": "150cm", "体重": "40kg", "血型": "B", "种族": "人族", "喜好": "看戏、扮家家酒", "声优": "植田佳奈", "称号": "知名女演员"},
    1022: {"名字": "依里", "公会": "恶魔伪王国军", "生日": "11月22日", "年龄": "13", "身高": "150cm", "体重": "40kg", "血型": "O", "种族": "魔族", "喜好": "所有游戏", "声优": "原纱友里", "妹妹": "茜里", "性格": "害羞", "称号": "天才玩家"},
    1023: {"名字": "绫音", "公会": "咲恋救济院", "生日": "5月10日", "年龄": "14", "身高": "148cm", "体重": "38kg", "血型": "B", "种族": "人族", "喜好": "能在房间里玩的游戏", "声优": "芹泽优", "伙伴": "噗吉"},
    1025: {"名字": "铃莓", "公会": "咲恋救济院", "生日": "12月12日", "年龄": "15", "身高": "154cm", "体重": "43kg", "血型": "O", "种族": "人族", "喜好": "服侍", "声优": "悠木碧", "特点": "冒冒失失"},
    1026: {"名字": "铃", "公会": "伊丽莎白牧场", "生日": "1月1日", "年龄": "17", "身高": "144cm", "体重": "42kg", "血型": "B", "种族": "兽人族", "喜好": "红豆面包", "声优": "小岩井小鸟", "性格": "懒散"},
    1027: {"名字": "惠理子", "公会": "暮光流星群", "生日": "7月30日", "年龄": "16", "身高": "154cm", "体重": "43kg", "血型": "B", "种族": "魔族", "喜好": "实验、裁缝、料理", "声优": "桥本千波", "称号": "破坏者"},
    1028: {"名字": "咲恋", "公会": "咲恋救济院", "生日": "10月4日", "年龄": "17", "身高": "156cm", "体重": "43kg", "血型": "A", "种族": "精灵族", "喜好": "经营、茶会", "声优": "堀江由衣", "称号": "妈妈"},
    1029: {"名字": "望", "公会": "慈乐之音", "生日": "1月24日", "年龄": "17", "身高": "157cm", "体重": "40kg", "血型": "B", "种族": "人族", "喜好": "看舞台剧、跳舞", "声优": "日笠阳子", "称号": "超人气偶像"},
    1030: {"名字": "妮诺", "公会": "纯白之翼兰德索尔分部", "生日": "8月31日", "年龄": "16", "身高": "163cm", "体重": "51kg", "血型": "O", "种族": "人族", "喜好": "忍术开发", "声优": "佐藤聪美", "憧憬的地方": "东国", "称号": "冒牌忍者", "爱读的书": "《武士道》"},
    1031: {"名字": "忍", "公会": "恶魔伪王国军", "生日": "12月22日", "年龄": "18", "身高": "157cm", "体重": "42kg", "血型": "AB", "种族": "魔族", "喜好": "占卜", "声优": "大坪由佳", "称号": "占卜师"},
    1032: {"名字": "秋乃", "公会": "墨丘利财团", "生日": "3月12日", "年龄": "18", "身高": "157cm", "体重": "45kg", "血型": "AB", "种族": "人族", "喜好": "慈善事业", "声优": "松嵜丽", "称号": "大小姐"},
    1033: {"名字": "真阳", "公会": "伊丽莎白牧场", "生日": "3月3日", "年龄": "20", "身高": "142cm", "体重": "35kg", "血型": "B", "种族": "人族", "喜好": "相声", "声优": "新田惠海", "工作": "牧场主人", "职业道路": "搞笑艺人之路"},
    1034: {"名字": "优花梨", "公会": "墨丘利财团", "生日": "3月16日", "年龄": "22", "身高": "164cm", "体重": "55kg", "血型": "A", "种族": "精灵族", "喜好": "随意逛街", "声优": "今井麻美", "称号": "女中酒豪"},
    1036: {"名字": "镜华", "公会": "小小甜心", "生日": "2月2日", "年龄": "8", "身高": "118cm", "体重": "21kg", "血型": "A", "种族": "精灵族", "喜好": "读书", "声优": "小仓唯", "称号": "资优生"},
    1037: {"名字": "智", "公会": "王宫骑士团", "生日": "8月11日", "年龄": "13", "身高": "149cm", "体重": "43kg", "血型": "A", "种族": "人族", "喜好": "剑术、戏弄长者", "声优": "茅原实里", "家传剑技": "御久间流", "家传剑技的奥义": "阿修罗"},
    1038: {"名字": "栞", "公会": "伊丽莎白牧场", "生日": "11月3日", "年龄": "14", "身高": "153cm", "体重": "40kg", "血型": "A", "种族": "兽人族", "喜好": "读书、散步", "声优": "小清水亚美", "姊姊": "初音"},
    1040: {"名字": "碧", "公会": "森林守卫", "生日": "6月6日", "年龄": "13", "身高": "158cm", "体重": "44kg", "血型": "AB", "种族": "精灵族", "喜好": "交朋友的想象训练", "声优": "花泽香菜", "称号": "边缘人"},
    1042: {"名字": "千歌", "公会": "慈乐之音", "生日": "6月3日", "年龄": "17", "身高": "163cm", "体重": "46kg", "血型": "O", "种族": "人族", "喜好": "各种乐器", "声优": "福原绫香", "工作": "唱唤师", "称号": "歌姬"},
    1043: {"名字": "真琴", "公会": "自卫团", "生日": "8月9日", "年龄": "17", "身高": "168cm", "体重": "54kg", "血型": "O", "种族": "兽人族", "喜好": "做点心", "声优": "小松未可子", "儿时玩伴": "优衣"},
    1044: {"名字": "伊莉亚", "公会": "恶魔伪王国军", "生日": "5月5日", "年龄": "？？？", "身高": "172cm", "体重": "50kg", "血型": "A", "种族": "魔族", "喜好": "征服世界", "声优": "丹下樱", "称号": "传说的吸血鬼", "工作": "统领黑夜"},
    1045: {"名字": "空花", "公会": "纯白之翼兰德索尔分部", "生日": "11月19日", "年龄": "18", "身高": "157cm", "体重": "49kg", "血型": "AB", "种族": "人族", "喜好": "阅读小说", "声优": "长妻树里", "称号": "被虐狂"},
    1046: {"名字": "珠希", "公会": "墨丘利财团", "生日": "3月1日", "年龄": "18", "身高": "158cm", "体重": "48kg", "血型": "AB", "种族": "兽人族", "喜好": "与猫咪玩耍", "声优": "沼仓爱美", "外表": "猫娘", "称号": "幻影猫"},
    1047: {"名字": "纯", "公会": "王宫骑士团", "生日": "10月25日", "年龄": "25", "身高": "171cm", "体重": "50kg", "血型": "A", "种族": "人族", "喜好": "格斗技、入浴", "声优": "川澄绫子", "职位": "团长"},
    1048: {"名字": "美冬", "公会": "墨丘利财团", "生日": "11月11日", "年龄": "20", "身高": "163cm", "体重": "49kg", "血型": "O", "种族": "人族", "喜好": "佣兵等等的打工", "声优": "田所梓", "信条": "效率至上"},
    1049: {"名字": "静流", "公会": "拉比林斯", "生日": "10月24日", "年龄": "18", "身高": "168cm", "体重": "54kg", "血型": "O", "种族": "人族", "喜好": "所有家事", "声优": "生天目仁美", "自称": "姐姐"},
    1050: {"名字": "美咲", "公会": "月光学院", "生日": "1月3日", "年龄": "11", "身高": "120cm", "体重": "22kg", "血型": "A", "种族": "魔族", "喜好": "阅读流行杂志、搜集化妆品", "声优": "久野美咲", "自称": "成熟的淑女"},
    1051: {"名字": "深月", "公会": "暮光流星群", "生日": "3月7日", "年龄": "27", "身高": "166cm", "体重": "53kg", "血型": "A", "种族": "人族", "喜好": "研究、实验", "声优": "三石琴乃", "工作": "疯狂科学家", "称号": "独眼恶魔"},
    1052: {"名字": "莉玛", "公会": "伊丽莎白牧场", "生日": "3月14日", "年龄": "18", "身高": "150cm", "体重": "100kg", "血型": "A", "种族": "兽人族", "喜好": "理毛、聊天", "声优": "德井青空", "特点": "毛茸茸"},
    1053: {"名字": "莫妮卡", "公会": "纯白之翼兰德索尔分部", "生日": "7月28日", "年龄": "18", "身高": "140cm", "体重": "33kg", "血型": "A", "种族": "人族", "喜好": "逛糖果店", "声优": "辻亚由美", "称号": "小鬼头"},
    1054: {"名字": "纺希", "公会": "慈乐之音", "生日": "9月7日", "年龄": "14", "身高": "153cm", "体重": "45kg", "血型": "AB", "种族": "人族", "喜好": "裁缝", "声优": "木户衣吹", "创办的组织": "怜大人粉丝俱乐部"},
    1055: {"名字": "步未", "公会": "纯白之翼兰德索尔分部", "生日": "4月7日", "年龄": "16", "身高": "155cm", "体重": "43kg", "血型": "O", "种族": "精灵族", "喜好": "观察", "声优": "大关英里", "称号": "跟踪狂"},
    1056: {"名字": "流夏", "公会": "暮光流星群", "生日": "7月11日", "年龄": "25", "身高": "167cm", "体重": "54kg", "血型": "B", "种族": "人族", "喜好": "钓鱼", "声优": "佐藤利奈", "称号": "大姐头"},
    1057: {"名字": "吉塔", "公会": "？？？", "生日": "3月10日", "年龄": "17", "身高": "156cm", "体重": "45kg", "血型": "O", "种族": "人族", "喜好": "冒险、聊天", "声优": "金元寿子", "称号": "苍空的骑空士"},
    1058: {"名字": "贪吃佩可", "公会": "美食殿堂", "生日": "3月31日", "年龄": "17", "身高": "156cm", "体重": "46kg", "血型": "O", "种族": "人族", "喜好": "边走边吃、料理", "声优": "M·A·O", "口头禅": "太赞了吧☆", "装备": "皇家装备", "身份": "阿斯特赖亚王家的王女"},
    1059: {"名字": "可可萝", "公会": "美食殿堂", "生日": "5月11日", "年龄": "11", "身高": "140cm", "体重": "35kg", "血型": "B", "种族": "精灵族", "喜好": "冥想、养育动植物", "声优": "伊藤美来", "职责": "向导", "工作": "巫女"},
    1060: {"名字": "凯留", "公会": "美食殿堂", "生日": "9月2日", "年龄": "14", "身高": "152cm", "体重": "39kg", "血型": "A", "种族": "兽人族", "喜好": "和猫咪玩耍", "声优": "立花理香", "性格特点": "傲娇"},
    1061: {"名字": "矛依未", "公会": "？？？", "生日": "8月11日", "年龄": "16", "身高": "148cm", "体重": "40kg", "血型": "O", "种族": "人族", "喜好": "冒险、回忆故事", "声优": "潘惠美", "真正的名字": "诺维姆"},
    1063: {"名字": "亚里莎", "公会": "？？？", "生日": "6月17日", "年龄": "15", "身高": "155cm", "体重": "42kg", "血型": "O", "种族": "精灵族", "喜好": "搜集漂亮的叶子", "声优": "优木加奈", "称号": "见习森林守卫"},
    1064: {"名字": "雪菲", "公会": "美食殿堂", "生日": "？月？日", "年龄": "？？", "身高": "147cm", "体重": "？？？", "血型": "？", "种族": "龙人族", "喜好": "读书、伸展运动", "声优": "近藤玲奈", "称号": "失去记忆的龙女"},   
    1065: {"名字": "嘉夜", "公会": "龙族巢穴", "生日": "6月25日", "年龄": "16", "身高": "156cm", "体重": "？？？kg", "血型": "B", "种族": "龙人族", "喜好": "格斗技", "声优": "小市真琴", "称号": "笨蛋打架狂"},
    1066: {"名字": "祈梨", "公会": "龙族巢穴", "生日": "9月29日", "年龄": "13", "身高": "145cm", "体重": "？？？kg", "血型": "AB", "种族": "龙人族", "喜好": "游戏", "声优": "藤田茜", "特技": "龙之吐息", "职位": "干部"},
    1067: {"名字": "帆稀", "公会": "龙族巢穴", "生日": "4月17日", "年龄": "25", "身高": "168cm", "体重": "？？？kg", "血型": "O", "种族": "龙族", "喜好": "绘画、读书", "声优": "大西沙织", "称号": "卧龙头领"},
    1068: {"名字": "菈比莉斯塔", "公会": "拉比林斯", "生日": "7月25日", "年龄": "25", "身高": "160cm", "体重": "？？？kg", "血型": "AB", "种族": "人族", "喜好": "观察人类", "声优": "泽城美雪", "称号": "秘密结社拉比林斯的「迷宫女王」"},
    1069: {"名字": "真那", "公会": "？？？", "生日": "7月1日", "年龄": "29", "身高": "166cm", "体重": "？？？kg", "血型": "AB", "种族": "兽人族", "喜好": "占卜、支配", "声优": "仓井翔太", "称号": "笼罩在神秘中的兰德索尔之王"},
    1070: {"名字": "似似花", "公会": "？？？", "生日": "3月24日", "年龄": "24", "身高": "149cm", "体重": "？？？kg", "血型": "O", "种族": "精灵族", "喜好": "模仿、艺术欣赏", "声优": "井口裕香", "称号": "变貌大妃", "特技": "分身"},
    1071: {"名字": "克莉丝提娜", "公会": "王宫骑士团", "生日": "2月7日", "年龄": "27", "身高": "165cm", "体重": "？？？kg", "血型": "O", "种族": "人族", "喜好": "和强敌之间的竞争", "声优": "高桥智秋", "称号": "誓约女君", "职位": "副团长"},
    1092: {"名字": "安", "公会": "？？？", "生日": "12月1日", "年龄": "17", "身高": "156cm", "体重": "55kg", "血型": "AB", "种族": "人族", "喜好": "读书", "声优": "日笠阳子"},
    1093: {"名字": "露", "公会": "？？？", "生日": "2月4日", "年龄": "15", "身高": "144cm", "体重": "45kg", "血型": "O", "种族": "人族", "喜好": "吃饭、睡觉", "声优": "古山贵实子"},
    1094: {"名字": "古蕾娅", "公会": "？？？", "生日": "11月3日", "年龄": "17", "身高": "167cm", "体重": "67kg", "血型": "B", "种族": "半人半龙", "喜好": "钢琴", "声优": "福原绫香"},
    1097: {"名字": "雷姆", "公会": "？？？", "生日": "2月2日", "年龄": "17", "身高": "154cm", "体重": "？？？kg", "血型": "？？？", "种族": "鬼族", "喜好": "戏剧欣赏、诗和散文", "声优": "水濑祈"},
    1098: {"名字": "拉姆", "公会": "？？？", "生日": "2月2日", "年龄": "17", "身高": "154cm", "体重": "？？？kg", "血型": "？？？", "种族": "鬼族", "喜好": "读书", "声优": "村川梨衣"},
    1099: {"名字": "爱蜜莉雅", "公会": "？？？", "生日": "9月23日", "年龄": "114", "身高": "164cm", "体重": "？？？kg", "血型": "？？？", "种族": "半精灵族", "喜好": "帮帕克梳理毛发、念书", "声优": "高桥李依"},
    1108: {"名字": "克萝依", "公会": "圣特蕾莎女子学院(好朋友社)", "生日": "8月7日", "年龄": "17", "身高": "154cm", "体重": "42kg", "血型": "O", "种族": "精灵族", "喜好": "飞镖", "声优": "种崎敦美", "性格特点": "阴暗系", "称号": "圣德蕾女的狂人"},
    1109: {"名字": "琪爱儿", "公会": "圣特蕾莎女子学院(好朋友社)", "生日": "9月15日", "年龄": "16", "身高": "156cm", "体重": "46kg", "血型": "O", "种族": "人族", "喜好": "跳舞、卡拉OK", "声优": "佐仓绫音", "切嚕唎咧咧囉唎囉唎囉": "咧切嚕切嚕啵啪嗶", "称号": "圣德蕾女的狂人"},
    1110: {"名字": "优妮", "公会": "圣特蕾莎女子学院(好朋友社)", "生日": "2月28日", "年龄": "18", "身高": "142cm", "体重": "36kg", "血型": "O", "种族": "人族", "喜好": "读书", "声优": "小原好美", "生活习惯": "茧居族", "称号": "圣德蕾女的狂人"},
    1114: {"名字": "露娜", "公会": "？？？", "生日": "？？？", "年龄": "？？？", "身高": "142cm", "体重": "28kg", "血型": "？？？", "种族": "人族", "喜好": "找「朋友」之事", "声优": "小仓唯"},
    1124: {"名字": "卯月", "公会": "NewGeneration", "生日": "4月24日", "年龄": "17", "身高": "159cm", "体重": "45kg", "血型": "O", "种族": "人族", "喜好": "和朋友打长电话", "声优": "大桥彩香"},
    1125: {"名字": "凛", "公会": "NewGeneration", "生日": "8月10日", "年龄": "15", "身高": "165cm", "体重": "44kg", "血型": "B", "种族": "人族", "喜好": "带狗散步", "声优": "福原绫香"},
    1126: {"名字": "未央", "公会": "NewGeneration", "生日": "12月1日", "年龄": "15", "身高": "161cm", "体重": "46kg", "血型": "B", "种族": "人族", "喜好": "购物", "声优": "原纱友里"},
    1180: {"名字": "克蕾琪塔", "公会": "里士满工商会", "生日": "9月19日", "年龄": "26", "身高": "160cm", "体重": "57kg", "血型": "A", "种族": "人族", "喜好": "数钱、打坏主意", "声优": "Lynn", "称号": "觉醒忠义的女商人"},
    1181: {"名字": "兰法", "公会": "愤怒·军团", "生日": "12月28日", "年龄": "20", "身高": "165cm", "体重": "53kg", "血型": "O", "种族": "魔族", "喜好": "唱歌、看书，以及写诗", "声优": "原田彩枫", "称号": "追求安静而歌唱的忧郁少女"},
    1182: {"名字": "美空", "公会": "愤怒·军团", "生日": "7月2日", "年龄": "16", "身高": "159cm", "体重": "？？？kg", "血型": "A", "种族": "人族", "喜好": "没有特别的爱好", "声优": "鬼头明里", "称号": "开朗活泼，但擅于毁灭的少女"},
    1185: {"名字": "花凛", "公会": "？？？", "生日": "9月12日", "年龄": "24", "身高": "152cm", "体重": "43kg", "血型": "A", "种族": "人族", "喜好": "处理文件、散步、桌游", "声优": "洲崎绫", "称号": "【公会管理协会】好心的接待员姐姐"},
    1230: {"名字": "爱梅斯", "公会": "？？？", "生日": "？月？日", "年龄": "？？？", "身高": "150cm", "体重": "？？？kg", "血型": "？", "种族": "？？？", "喜好": "？？？", "声优": "相坂优歌", "称号": "以崭新的姿态支撑骑士冒险的妖精"},
    1223: {"名字": "斑比", "公会": "？？？", "生日": "？月？日", "年龄": "？？？", "身高": "149cm", "体重": "41kg", "血型": "AB", "种族": "魔族", "喜好": "散步、做饭", "声优": "钉宫理惠", "称号": "眷属的主人"},
    1233: {"名字": "涅娅", "公会": "愤怒·军团", "生日": "6月13日", "年龄": "19", "身高": "157cm", "体重": "55kg", "血型": "B", "种族": "魔族？", "喜好": "和可爱的正太玩耍、购物", "声优": "和气杏未", "称号": "最喜欢正太的史莱姆辣妹♪"},    
}
