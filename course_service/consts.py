GET_COURSES_BY_SCHOOL_CACHE_PREFIX = "GET_COURSES_BY_SCHOOL"
GET_TEACHER_NAMES_CACHE_PREFIX = "GET_TEACHER_NAMES"
GET_TEACHER_IDS_BY_COURSE_ID_CACHE_PREFIX = "GET_TEACHER_IDS_BY_COURSE_ID"
GET_COURSE_RANK_CACHE_PREFIX = "GET_COURSE_RANK"

GET_COURSES_BY_SCHOOL_CACHE_TIMEOUT = 60 * 30
GET_TEACHER_NAMES_CACHE_TIMEOUT = 60 * 30
GET_TEACHER_IDS_BY_COURSE_ID_CACHE_TIMEOUT = 60 * 30
GET_COURSE_RANK_CACHE_TIMEOUT = 60 * 5

SchoolEnum = {
	"数学科学学院": 1,
	"物理学院": 2,
	"化学与分子工程学院": 3,
	"生命科学学院": 4,
	"地球与空间科学学院": 5,
	"心理与认知科学学院": 6,
	"软件与微电子学院": 7,
	"新闻与传播学院": 8,
	"中国语言文学系": 9,
	"历史学系": 10,
	"考古文博学院": 11,
	"哲学系（宗教学系）": 12,
	"国际关系学院": 13,
	"经济学院": 14,
	"光华管理学院": 15,
	"法学院": 16,
	"信息管理系": 17,
	"社会学系": 18,
	"政府管理学院": 19,
	"英语语言文学系": 20,
	"外国语学院": 21,
	"马克思主义学院": 22,
	"体育教研部": 23,
	"艺术学院": 24,
	"对外汉语教育学院": 25,
	"元培学院": 26,
	"深圳研究生院": 27,
	"信息科学技术学院": 28,
	"国家发展研究院": 29,
	"教育学院": 30,
	"人口研究所": 31,
	"前沿交叉学科研究院": 32,
	"工学院": 33,
	"城市与环境学院": 34,
	"环境科学与工程学院": 35,
	"医学部教学办": 36,
	"分子医学研究所": 37,
	"歌剧研究院": 38,
	"建筑与景观设计学院": 39,
	"新媒体研究院": 40,
	"燕京学堂": 41,
	"现代农学院（筹）": 42,
	"武装部": 43,
	"国际合作部": 44,
	"教务部": 45,
	"研究生院": 46,
	"创新创业学院": 47,
	"哲学系": 48,
	"现代农学院": 49,
	"学生工作部人民武装部": 50,
}


CourseTypeEnum = {
	"专业课": 100,
	"政治课": 200,
	"英语课": 300,
	"英语课A": 301,
	"英语课B": 302,
	"英语课C": 303,
	"英语课C+": 304,
	"体育课": 400,
	"通选课": 500,
	"通选课A": 501,
	"通选课B": 502,
	"通选课C": 503,
	"通选课D": 504,
	"通选课E": 505,
	"通选课F": 506,
	"公选课": 600,
	"计算机基础课": 700,
}