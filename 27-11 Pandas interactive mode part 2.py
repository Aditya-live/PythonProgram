Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd

>>> 
>>> 
>>> pd.to_datetime(pd.Series(['2017-04-01','2017-04-02','2017-04-03']))
0   2017-04-01
1   2017-04-02
2   2017-04-03
dtype: datetime64[ns]
>>> 
>>> #Renaming a specific column
>>> 
>>> res=pd.DataFrame({'weekday':[1,2,3,4,5,6],'name':['sun','mon','tues','wed','thu','fri']})
>>> res
   weekday  name
0        1   sun
1        2   mon
2        3  tues
3        4   wed
4        5   thu
5        6   fri
>>> res.rename(columns={'weekday':'dayno'})
   dayno  name
0      1   sun
1      2   mon
2      3  tues
3      4   wed
4      5   thu
5      6   fri
>>> 
>>> res.loc[6]=[7,'sat']
>>> 
>>> res
   weekday  name
0        1   sun
1        2   mon
2        3  tues
3        4   wed
4        5   thu
5        6   fri
6        7   sat
>>> #Above func to add row
>>> 
>>> res.loc[7]=[1,'sun']
>>> res
   weekday  name
0        1   sun
1        2   mon
2        3  tues
3        4   wed
4        5   thu
5        6   fri
6        7   sat
7        1   sun
>>> #For checking duplicate entries
>>> res.duplicated()
0    False
1    False
2    False
3    False
4    False
5    False
6    False
7     True
dtype: bool
>>> 
>>> res.loc[8]=[7,'sat']
>>> res.duplicated()
0    False
1    False
2    False
3    False
4    False
5    False
6    False
7     True
8     True
dtype: bool
>>> # Deleting the duplicate values
>>> 
>>> res.drop_duplicates()
   weekday  name
0        1   sun
1        2   mon
2        3  tues
3        4   wed
4        5   thu
5        6   fri
6        7   sat
>>> 
>>> res=pd.read_csv("C://python37//Prog//Assignment 13//diabetes.csv")
>>> 
>>> pd.isnull(res)
     Pregnancies  Glucose  ...    Age  Outcome
0          False    False  ...  False    False
1          False    False  ...  False    False
2          False    False  ...  False    False
3          False    False  ...  False    False
4          False    False  ...  False    False
..           ...      ...  ...    ...      ...
763        False    False  ...  False    False
764        False    False  ...  False    False
765        False    False  ...  False    False
766        False    False  ...  False    False
767        False    False  ...  False    False

[768 rows x 9 columns]
>>> pd.set_option('display.max_rows',1000)
>>> pd.set_option('display.max_columns',1000)
>>> pd.set_option('display.max_colwidth',1000)
>>> pd.set_option('display.width',1000)
>>> pd.isnull(res)
     Pregnancies  Glucose  BloodPressure  SkinThickness  Insulin    BMI  DiabetesPedigreeFunction    Age  Outcome
0          False    False          False          False    False  False                     False  False    False
1          False    False          False          False    False  False                     False  False    False
2          False    False          False          False    False  False                     False  False    False
3          False    False          False          False    False  False                     False  False    False
4          False    False          False          False    False  False                     False  False    False
5          False    False          False          False    False  False                     False  False    False
6          False    False          False          False    False  False                     False  False    False
7          False    False          False          False    False  False                     False  False    False
8          False    False          False          False    False  False                     False  False    False
9          False    False          False          False    False  False                     False  False    False
10         False    False          False          False    False  False                     False  False    False
11         False    False          False          False    False  False                     False  False    False
12         False    False          False          False    False  False                     False  False    False
13         False    False          False          False    False  False                     False  False    False
14         False    False          False          False    False  False                     False  False    False
15         False    False          False          False    False  False                     False  False    False
16         False    False          False          False    False  False                     False  False    False
17         False    False          False          False    False  False                     False  False    False
18         False    False          False          False    False  False                     False  False    False
19         False    False          False          False    False  False                     False  False    False
20         False    False          False          False    False  False                     False  False    False
21         False    False          False          False    False  False                     False  False    False
22         False    False          False          False    False  False                     False  False    False
23         False    False          False          False    False  False                     False  False    False
24         False    False          False          False    False  False                     False  False    False
25         False    False          False          False    False  False                     False  False    False
26         False    False          False          False    False  False                     False  False    False
27         False    False          False          False    False  False                     False  False    False
28         False    False          False          False    False  False                     False  False    False
29         False    False          False          False    False  False                     False  False    False
30         False    False          False          False    False  False                     False  False    False
31         False    False          False          False    False  False                     False  False    False
32         False    False          False          False    False  False                     False  False    False
33         False    False          False          False    False  False                     False  False    False
34         False    False          False          False    False  False                     False  False    False
35         False    False          False          False    False  False                     False  False    False
36         False    False          False          False    False  False                     False  False    False
37         False    False          False          False    False  False                     False  False    False
38         False    False          False          False    False  False                     False  False    False
39         False    False          False          False    False  False                     False  False    False
40         False    False          False          False    False  False                     False  False    False
41         False    False          False          False    False  False                     False  False    False
42         False    False          False          False    False  False                     False  False    False
43         False    False          False          False    False  False                     False  False    False
44         False    False          False          False    False  False                     False  False    False
45         False    False          False          False    False  False                     False  False    False
46         False    False          False          False    False  False                     False  False    False
47         False    False          False          False    False  False                     False  False    False
48         False    False          False          False    False  False                     False  False    False
49         False    False          False          False    False  False                     False  False    False
50         False    False          False          False    False  False                     False  False    False
51         False    False          False          False    False  False                     False  False    False
52         False    False          False          False    False  False                     False  False    False
53         False    False          False          False    False  False                     False  False    False
54         False    False          False          False    False  False                     False  False    False
55         False    False          False          False    False  False                     False  False    False
56         False    False          False          False    False  False                     False  False    False
57         False    False          False          False    False  False                     False  False    False
58         False    False          False          False    False  False                     False  False    False
59         False    False          False          False    False  False                     False  False    False
60         False    False          False          False    False  False                     False  False    False
61         False    False          False          False    False  False                     False  False    False
62         False    False          False          False    False  False                     False  False    False
63         False    False          False          False    False  False                     False  False    False
64         False    False          False          False    False  False                     False  False    False
65         False    False          False          False    False  False                     False  False    False
66         False    False          False          False    False  False                     False  False    False
67         False    False          False          False    False  False                     False  False    False
68         False    False          False          False    False  False                     False  False    False
69         False    False          False          False    False  False                     False  False    False
70         False    False          False          False    False  False                     False  False    False
71         False    False          False          False    False  False                     False  False    False
72         False    False          False          False    False  False                     False  False    False
73         False    False          False          False    False  False                     False  False    False
74         False    False          False          False    False  False                     False  False    False
75         False    False          False          False    False  False                     False  False    False
76         False    False          False          False    False  False                     False  False    False
77         False    False          False          False    False  False                     False  False    False
78         False    False          False          False    False  False                     False  False    False
79         False    False          False          False    False  False                     False  False    False
80         False    False          False          False    False  False                     False  False    False
81         False    False          False          False    False  False                     False  False    False
82         False    False          False          False    False  False                     False  False    False
83         False    False          False          False    False  False                     False  False    False
84         False    False          False          False    False  False                     False  False    False
85         False    False          False          False    False  False                     False  False    False
86         False    False          False          False    False  False                     False  False    False
87         False    False          False          False    False  False                     False  False    False
88         False    False          False          False    False  False                     False  False    False
89         False    False          False          False    False  False                     False  False    False
90         False    False          False          False    False  False                     False  False    False
91         False    False          False          False    False  False                     False  False    False
92         False    False          False          False    False  False                     False  False    False
93         False    False          False          False    False  False                     False  False    False
94         False    False          False          False    False  False                     False  False    False
95         False    False          False          False    False  False                     False  False    False
96         False    False          False          False    False  False                     False  False    False
97         False    False          False          False    False  False                     False  False    False
98         False    False          False          False    False  False                     False  False    False
99         False    False          False          False    False  False                     False  False    False
100        False    False          False          False    False  False                     False  False    False
101        False    False          False          False    False  False                     False  False    False
102        False    False          False          False    False  False                     False  False    False
103        False    False          False          False    False  False                     False  False    False
104        False    False          False          False    False  False                     False  False    False
105        False    False          False          False    False  False                     False  False    False
106        False    False          False          False    False  False                     False  False    False
107        False    False          False          False    False  False                     False  False    False
108        False    False          False          False    False  False                     False  False    False
109        False    False          False          False    False  False                     False  False    False
110        False    False          False          False    False  False                     False  False    False
111        False    False          False          False    False  False                     False  False    False
112        False    False          False          False    False  False                     False  False    False
113        False    False          False          False    False  False                     False  False    False
114        False    False          False          False    False  False                     False  False    False
115        False    False          False          False    False  False                     False  False    False
116        False    False          False          False    False  False                     False  False    False
117        False    False          False          False    False  False                     False  False    False
118        False    False          False          False    False  False                     False  False    False
119        False    False          False          False    False  False                     False  False    False
120        False    False          False          False    False  False                     False  False    False
121        False    False          False          False    False  False                     False  False    False
122        False    False          False          False    False  False                     False  False    False
123        False    False          False          False    False  False                     False  False    False
124        False    False          False          False    False  False                     False  False    False
125        False    False          False          False    False  False                     False  False    False
126        False    False          False          False    False  False                     False  False    False
127        False    False          False          False    False  False                     False  False    False
128        False    False          False          False    False  False                     False  False    False
129        False    False          False          False    False  False                     False  False    False
130        False    False          False          False    False  False                     False  False    False
131        False    False          False          False    False  False                     False  False    False
132        False    False          False          False    False  False                     False  False    False
133        False    False          False          False    False  False                     False  False    False
134        False    False          False          False    False  False                     False  False    False
135        False    False          False          False    False  False                     False  False    False
136        False    False          False          False    False  False                     False  False    False
137        False    False          False          False    False  False                     False  False    False
138        False    False          False          False    False  False                     False  False    False
139        False    False          False          False    False  False                     False  False    False
140        False    False          False          False    False  False                     False  False    False
141        False    False          False          False    False  False                     False  False    False
142        False    False          False          False    False  False                     False  False    False
143        False    False          False          False    False  False                     False  False    False
144        False    False          False          False    False  False                     False  False    False
145        False    False          False          False    False  False                     False  False    False
146        False    False          False          False    False  False                     False  False    False
147        False    False          False          False    False  False                     False  False    False
148        False    False          False          False    False  False                     False  False    False
149        False    False          False          False    False  False                     False  False    False
150        False    False          False          False    False  False                     False  False    False
151        False    False          False          False    False  False                     False  False    False
152        False    False          False          False    False  False                     False  False    False
153        False    False          False          False    False  False                     False  False    False
154        False    False          False          False    False  False                     False  False    False
155        False    False          False          False    False  False                     False  False    False
156        False    False          False          False    False  False                     False  False    False
157        False    False          False          False    False  False                     False  False    False
158        False    False          False          False    False  False                     False  False    False
159        False    False          False          False    False  False                     False  False    False
160        False    False          False          False    False  False                     False  False    False
161        False    False          False          False    False  False                     False  False    False
162        False    False          False          False    False  False                     False  False    False
163        False    False          False          False    False  False                     False  False    False
164        False    False          False          False    False  False                     False  False    False
165        False    False          False          False    False  False                     False  False    False
166        False    False          False          False    False  False                     False  False    False
167        False    False          False          False    False  False                     False  False    False
168        False    False          False          False    False  False                     False  False    False
169        False    False          False          False    False  False                     False  False    False
170        False    False          False          False    False  False                     False  False    False
171        False    False          False          False    False  False                     False  False    False
172        False    False          False          False    False  False                     False  False    False
173        False    False          False          False    False  False                     False  False    False
174        False    False          False          False    False  False                     False  False    False
175        False    False          False          False    False  False                     False  False    False
176        False    False          False          False    False  False                     False  False    False
177        False    False          False          False    False  False                     False  False    False
178        False    False          False          False    False  False                     False  False    False
179        False    False          False          False    False  False                     False  False    False
180        False    False          False          False    False  False                     False  False    False
181        False    False          False          False    False  False                     False  False    False
182        False    False          False          False    False  False                     False  False    False
183        False    False          False          False    False  False                     False  False    False
184        False    False          False          False    False  False                     False  False    False
185        False    False          False          False    False  False                     False  False    False
186        False    False          False          False    False  False                     False  False    False
187        False    False          False          False    False  False                     False  False    False
188        False    False          False          False    False  False                     False  False    False
189        False    False          False          False    False  False                     False  False    False
190        False    False          False          False    False  False                     False  False    False
191        False    False          False          False    False  False                     False  False    False
192        False    False          False          False    False  False                     False  False    False
193        False    False          False          False    False  False                     False  False    False
194        False    False          False          False    False  False                     False  False    False
195        False    False          False          False    False  False                     False  False    False
196        False    False          False          False    False  False                     False  False    False
197        False    False          False          False    False  False                     False  False    False
198        False    False          False          False    False  False                     False  False    False
199        False    False          False          False    False  False                     False  False    False
200        False    False          False          False    False  False                     False  False    False
201        False    False          False          False    False  False                     False  False    False
202        False    False          False          False    False  False                     False  False    False
203        False    False          False          False    False  False                     False  False    False
204        False    False          False          False    False  False                     False  False    False
205        False    False          False          False    False  False                     False  False    False
206        False    False          False          False    False  False                     False  False    False
207        False    False          False          False    False  False                     False  False    False
208        False    False          False          False    False  False                     False  False    False
209        False    False          False          False    False  False                     False  False    False
210        False    False          False          False    False  False                     False  False    False
211        False    False          False          False    False  False                     False  False    False
212        False    False          False          False    False  False                     False  False    False
213        False    False          False          False    False  False                     False  False    False
214        False    False          False          False    False  False                     False  False    False
215        False    False          False          False    False  False                     False  False    False
216        False    False          False          False    False  False                     False  False    False
217        False    False          False          False    False  False                     False  False    False
218        False    False          False          False    False  False                     False  False    False
219        False    False          False          False    False  False                     False  False    False
220        False    False          False          False    False  False                     False  False    False
221        False    False          False          False    False  False                     False  False    False
222        False    False          False          False    False  False                     False  False    False
223        False    False          False          False    False  False                     False  False    False
224        False    False          False          False    False  False                     False  False    False
225        False    False          False          False    False  False                     False  False    False
226        False    False          False          False    False  False                     False  False    False
227        False    False          False          False    False  False                     False  False    False
228        False    False          False          False    False  False                     False  False    False
229        False    False          False          False    False  False                     False  False    False
230        False    False          False          False    False  False                     False  False    False
231        False    False          False          False    False  False                     False  False    False
232        False    False          False          False    False  False                     False  False    False
233        False    False          False          False    False  False                     False  False    False
234        False    False          False          False    False  False                     False  False    False
235        False    False          False          False    False  False                     False  False    False
236        False    False          False          False    False  False                     False  False    False
237        False    False          False          False    False  False                     False  False    False
238        False    False          False          False    False  False                     False  False    False
239        False    False          False          False    False  False                     False  False    False
240        False    False          False          False    False  False                     False  False    False
241        False    False          False          False    False  False                     False  False    False
242        False    False          False          False    False  False                     False  False    False
243        False    False          False          False    False  False                     False  False    False
244        False    False          False          False    False  False                     False  False    False
245        False    False          False          False    False  False                     False  False    False
246        False    False          False          False    False  False                     False  False    False
247        False    False          False          False    False  False                     False  False    False
248        False    False          False          False    False  False                     False  False    False
249        False    False          False          False    False  False                     False  False    False
250        False    False          False          False    False  False                     False  False    False
251        False    False          False          False    False  False                     False  False    False
252        False    False          False          False    False  False                     False  False    False
253        False    False          False          False    False  False                     False  False    False
254        False    False          False          False    False  False                     False  False    False
255        False    False          False          False    False  False                     False  False    False
256        False    False          False          False    False  False                     False  False    False
257        False    False          False          False    False  False                     False  False    False
258        False    False          False          False    False  False                     False  False    False
259        False    False          False          False    False  False                     False  False    False
260        False    False          False          False    False  False                     False  False    False
261        False    False          False          False    False  False                     False  False    False
262        False    False          False          False    False  False                     False  False    False
263        False    False          False          False    False  False                     False  False    False
264        False    False          False          False    False  False                     False  False    False
265        False    False          False          False    False  False                     False  False    False
266        False    False          False          False    False  False                     False  False    False
267        False    False          False          False    False  False                     False  False    False
268        False    False          False          False    False  False                     False  False    False
269        False    False          False          False    False  False                     False  False    False
270        False    False          False          False    False  False                     False  False    False
271        False    False          False          False    False  False                     False  False    False
272        False    False          False          False    False  False                     False  False    False
273        False    False          False          False    False  False                     False  False    False
274        False    False          False          False    False  False                     False  False    False
275        False    False          False          False    False  False                     False  False    False
276        False    False          False          False    False  False                     False  False    False
277        False    False          False          False    False  False                     False  False    False
278        False    False          False          False    False  False                     False  False    False
279        False    False          False          False    False  False                     False  False    False
280        False    False          False          False    False  False                     False  False    False
281        False    False          False          False    False  False                     False  False    False
282        False    False          False          False    False  False                     False  False    False
283        False    False          False          False    False  False                     False  False    False
284        False    False          False          False    False  False                     False  False    False
285        False    False          False          False    False  False                     False  False    False
286        False    False          False          False    False  False                     False  False    False
287        False    False          False          False    False  False                     False  False    False
288        False    False          False          False    False  False                     False  False    False
289        False    False          False          False    False  False                     False  False    False
290        False    False          False          False    False  False                     False  False    False
291        False    False          False          False    False  False                     False  False    False
292        False    False          False          False    False  False                     False  False    False
293        False    False          False          False    False  False                     False  False    False
294        False    False          False          False    False  False                     False  False    False
295        False    False          False          False    False  False                     False  False    False
296        False    False          False          False    False  False                     False  False    False
297        False    False          False          False    False  False                     False  False    False
298        False    False          False          False    False  False                     False  False    False
299        False    False          False          False    False  False                     False  False    False
300        False    False          False          False    False  False                     False  False    False
301        False    False          False          False    False  False                     False  False    False
302        False    False          False          False    False  False                     False  False    False
303        False    False          False          False    False  False                     False  False    False
304        False    False          False          False    False  False                     False  False    False
305        False    False          False          False    False  False                     False  False    False
306        False    False          False          False    False  False                     False  False    False
307        False    False          False          False    False  False                     False  False    False
308        False    False          False          False    False  False                     False  False    False
309        False    False          False          False    False  False                     False  False    False
310        False    False          False          False    False  False                     False  False    False
311        False    False          False          False    False  False                     False  False    False
312        False    False          False          False    False  False                     False  False    False
313        False    False          False          False    False  False                     False  False    False
314        False    False          False          False    False  False                     False  False    False
315        False    False          False          False    False  False                     False  False    False
316        False    False          False          False    False  False                     False  False    False
317        False    False          False          False    False  False                     False  False    False
318        False    False          False          False    False  False                     False  False    False
319        False    False          False          False    False  False                     False  False    False
320        False    False          False          False    False  False                     False  False    False
321        False    False          False          False    False  False                     False  False    False
322        False    False          False          False    False  False                     False  False    False
323        False    False          False          False    False  False                     False  False    False
324        False    False          False          False    False  False                     False  False    False
325        False    False          False          False    False  False                     False  False    False
326        False    False          False          False    False  False                     False  False    False
327        False    False          False          False    False  False                     False  False    False
328        False    False          False          False    False  False                     False  False    False
329        False    False          False          False    False  False                     False  False    False
330        False    False          False          False    False  False                     False  False    False
331        False    False          False          False    False  False                     False  False    False
332        False    False          False          False    False  False                     False  False    False
333        False    False          False          False    False  False                     False  False    False
334        False    False          False          False    False  False                     False  False    False
335        False    False          False          False    False  False                     False  False    False
336        False    False          False          False    False  False                     False  False    False
337        False    False          False          False    False  False                     False  False    False
338        False    False          False          False    False  False                     False  False    False
339        False    False          False          False    False  False                     False  False    False
340        False    False          False          False    False  False                     False  False    False
341        False    False          False          False    False  False                     False  False    False
342        False    False          False          False    False  False                     False  False    False
343        False    False          False          False    False  False                     False  False    False
344        False    False          False          False    False  False                     False  False    False
345        False    False          False          False    False  False                     False  False    False
346        False    False          False          False    False  False                     False  False    False
347        False    False          False          False    False  False                     False  False    False
348        False    False          False          False    False  False                     False  False    False
349        False    False          False          False    False  False                     False  False    False
350        False    False          False          False    False  False                     False  False    False
351        False    False          False          False    False  False                     False  False    False
352        False    False          False          False    False  False                     False  False    False
353        False    False          False          False    False  False                     False  False    False
354        False    False          False          False    False  False                     False  False    False
355        False    False          False          False    False  False                     False  False    False
356        False    False          False          False    False  False                     False  False    False
357        False    False          False          False    False  False                     False  False    False
358        False    False          False          False    False  False                     False  False    False
359        False    False          False          False    False  False                     False  False    False
360        False    False          False          False    False  False                     False  False    False
361        False    False          False          False    False  False                     False  False    False
362        False    False          False          False    False  False                     False  False    False
363        False    False          False          False    False  False                     False  False    False
364        False    False          False          False    False  False                     False  False    False
365        False    False          False          False    False  False                     False  False    False
366        False    False          False          False    False  False                     False  False    False
367        False    False          False          False    False  False                     False  False    False
368        False    False          False          False    False  False                     False  False    False
369        False    False          False          False    False  False                     False  False    False
370        False    False          False          False    False  False                     False  False    False
371        False    False          False          False    False  False                     False  False    False
372        False    False          False          False    False  False                     False  False    False
373        False    False          False          False    False  False                     False  False    False
374        False    False          False          False    False  False                     False  False    False
375        False    False          False          False    False  False                     False  False    False
376        False    False          False          False    False  False                     False  False    False
377        False    False          False          False    False  False                     False  False    False
378        False    False          False          False    False  False                     False  False    False
379        False    False          False          False    False  False                     False  False    False
380        False    False          False          False    False  False                     False  False    False
381        False    False          False          False    False  False                     False  False    False
382        False    False          False          False    False  False                     False  False    False
383        False    False          False          False    False  False                     False  False    False
384        False    False          False          False    False  False                     False  False    False
385        False    False          False          False    False  False                     False  False    False
386        False    False          False          False    False  False                     False  False    False
387        False    False          False          False    False  False                     False  False    False
388        False    False          False          False    False  False                     False  False    False
389        False    False          False          False    False  False                     False  False    False
390        False    False          False          False    False  False                     False  False    False
391        False    False          False          False    False  False                     False  False    False
392        False    False          False          False    False  False                     False  False    False
393        False    False          False          False    False  False                     False  False    False
394        False    False          False          False    False  False                     False  False    False
395        False    False          False          False    False  False                     False  False    False
396        False    False          False          False    False  False                     False  False    False
397        False    False          False          False    False  False                     False  False    False
398        False    False          False          False    False  False                     False  False    False
399        False    False          False          False    False  False                     False  False    False
400        False    False          False          False    False  False                     False  False    False
401        False    False          False          False    False  False                     False  False    False
402        False    False          False          False    False  False                     False  False    False
403        False    False          False          False    False  False                     False  False    False
404        False    False          False          False    False  False                     False  False    False
405        False    False          False          False    False  False                     False  False    False
406        False    False          False          False    False  False                     False  False    False
407        False    False          False          False    False  False                     False  False    False
408        False    False          False          False    False  False                     False  False    False
409        False    False          False          False    False  False                     False  False    False
410        False    False          False          False    False  False                     False  False    False
411        False    False          False          False    False  False                     False  False    False
412        False    False          False          False    False  False                     False  False    False
413        False    False          False          False    False  False                     False  False    False
414        False    False          False          False    False  False                     False  False    False
415        False    False          False          False    False  False                     False  False    False
416        False    False          False          False    False  False                     False  False    False
417        False    False          False          False    False  False                     False  False    False
418        False    False          False          False    False  False                     False  False    False
419        False    False          False          False    False  False                     False  False    False
420        False    False          False          False    False  False                     False  False    False
421        False    False          False          False    False  False                     False  False    False
422        False    False          False          False    False  False                     False  False    False
423        False    False          False          False    False  False                     False  False    False
424        False    False          False          False    False  False                     False  False    False
425        False    False          False          False    False  False                     False  False    False
426        False    False          False          False    False  False                     False  False    False
427        False    False          False          False    False  False                     False  False    False
428        False    False          False          False    False  False                     False  False    False
429        False    False          False          False    False  False                     False  False    False
430        False    False          False          False    False  False                     False  False    False
431        False    False          False          False    False  False                     False  False    False
432        False    False          False          False    False  False                     False  False    False
433        False    False          False          False    False  False                     False  False    False
434        False    False          False          False    False  False                     False  False    False
435        False    False          False          False    False  False                     False  False    False
436        False    False          False          False    False  False                     False  False    False
437        False    False          False          False    False  False                     False  False    False
438        False    False          False          False    False  False                     False  False    False
439        False    False          False          False    False  False                     False  False    False
440        False    False          False          False    False  False                     False  False    False
441        False    False          False          False    False  False                     False  False    False
442        False    False          False          False    False  False                     False  False    False
443        False    False          False          False    False  False                     False  False    False
444        False    False          False          False    False  False                     False  False    False
445        False    False          False          False    False  False                     False  False    False
446        False    False          False          False    False  False                     False  False    False
447        False    False          False          False    False  False                     False  False    False
448        False    False          False          False    False  False                     False  False    False
449        False    False          False          False    False  False                     False  False    False
450        False    False          False          False    False  False                     False  False    False
451        False    False          False          False    False  False                     False  False    False
452        False    False          False          False    False  False                     False  False    False
453        False    False          False          False    False  False                     False  False    False
454        False    False          False          False    False  False                     False  False    False
455        False    False          False          False    False  False                     False  False    False
456        False    False          False          False    False  False                     False  False    False
457        False    False          False          False    False  False                     False  False    False
458        False    False          False          False    False  False                     False  False    False
459        False    False          False          False    False  False                     False  False    False
460        False    False          False          False    False  False                     False  False    False
461        False    False          False          False    False  False                     False  False    False
462        False    False          False          False    False  False                     False  False    False
463        False    False          False          False    False  False                     False  False    False
464        False    False          False          False    False  False                     False  False    False
465        False    False          False          False    False  False                     False  False    False
466        False    False          False          False    False  False                     False  False    False
467        False    False          False          False    False  False                     False  False    False
468        False    False          False          False    False  False                     False  False    False
469        False    False          False          False    False  False                     False  False    False
470        False    False          False          False    False  False                     False  False    False
471        False    False          False          False    False  False                     False  False    False
472        False    False          False          False    False  False                     False  False    False
473        False    False          False          False    False  False                     False  False    False
474        False    False          False          False    False  False                     False  False    False
475        False    False          False          False    False  False                     False  False    False
476        False    False          False          False    False  False                     False  False    False
477        False    False          False          False    False  False                     False  False    False
478        False    False          False          False    False  False                     False  False    False
479        False    False          False          False    False  False                     False  False    False
480        False    False          False          False    False  False                     False  False    False
481        False    False          False          False    False  False                     False  False    False
482        False    False          False          False    False  False                     False  False    False
483        False    False          False          False    False  False                     False  False    False
484        False    False          False          False    False  False                     False  False    False
485        False    False          False          False    False  False                     False  False    False
486        False    False          False          False    False  False                     False  False    False
487        False    False          False          False    False  False                     False  False    False
488        False    False          False          False    False  False                     False  False    False
489        False    False          False          False    False  False                     False  False    False
490        False    False          False          False    False  False                     False  False    False
491        False    False          False          False    False  False                     False  False    False
492        False    False          False          False    False  False                     False  False    False
493        False    False          False          False    False  False                     False  False    False
494        False    False          False          False    False  False                     False  False    False
495        False    False          False          False    False  False                     False  False    False
496        False    False          False          False    False  False                     False  False    False
497        False    False          False          False    False  False                     False  False    False
498        False    False          False          False    False  False                     False  False    False
499        False    False          False          False    False  False                     False  False    False
500        False    False          False          False    False  False                     False  False    False
501        False    False          False          False    False  False                     False  False    False
502        False    False          False          False    False  False                     False  False    False
503        False    False          False          False    False  False                     False  False    False
504        False    False          False          False    False  False                     False  False    False
505        False    False          False          False    False  False                     False  False    False
506        False    False          False          False    False  False                     False  False    False
507        False    False          False          False    False  False                     False  False    False
508        False    False          False          False    False  False                     False  False    False
509        False    False          False          False    False  False                     False  False    False
510        False    False          False          False    False  False                     False  False    False
511        False    False          False          False    False  False                     False  False    False
512        False    False          False          False    False  False                     False  False    False
513        False    False          False          False    False  False                     False  False    False
514        False    False          False          False    False  False                     False  False    False
515        False    False          False          False    False  False                     False  False    False
516        False    False          False          False    False  False                     False  False    False
517        False    False          False          False    False  False                     False  False    False
518        False    False          False          False    False  False                     False  False    False
519        False    False          False          False    False  False                     False  False    False
520        False    False          False          False    False  False                     False  False    False
521        False    False          False          False    False  False                     False  False    False
522        False    False          False          False    False  False                     False  False    False
523        False    False          False          False    False  False                     False  False    False
524        False    False          False          False    False  False                     False  False    False
525        False    False          False          False    False  False                     False  False    False
526        False    False          False          False    False  False                     False  False    False
527        False    False          False          False    False  False                     False  False    False
528        False    False          False          False    False  False                     False  False    False
529        False    False          False          False    False  False                     False  False    False
530        False    False          False          False    False  False                     False  False    False
531        False    False          False          False    False  False                     False  False    False
532        False    False          False          False    False  False                     False  False    False
533        False    False          False          False    False  False                     False  False    False
534        False    False          False          False    False  False                     False  False    False
535        False    False          False          False    False  False                     False  False    False
536        False    False          False          False    False  False                     False  False    False
537        False    False          False          False    False  False                     False  False    False
538        False    False          False          False    False  False                     False  False    False
539        False    False          False          False    False  False                     False  False    False
540        False    False          False          False    False  False                     False  False    False
541        False    False          False          False    False  False                     False  False    False
542        False    False          False          False    False  False                     False  False    False
543        False    False          False          False    False  False                     False  False    False
544        False    False          False          False    False  False                     False  False    False
545        False    False          False          False    False  False                     False  False    False
546        False    False          False          False    False  False                     False  False    False
547        False    False          False          False    False  False                     False  False    False
548        False    False          False          False    False  False                     False  False    False
549        False    False          False          False    False  False                     False  False    False
550        False    False          False          False    False  False                     False  False    False
551        False    False          False          False    False  False                     False  False    False
552        False    False          False          False    False  False                     False  False    False
553        False    False          False          False    False  False                     False  False    False
554        False    False          False          False    False  False                     False  False    False
555        False    False          False          False    False  False                     False  False    False
556        False    False          False          False    False  False                     False  False    False
557        False    False          False          False    False  False                     False  False    False
558        False    False          False          False    False  False                     False  False    False
559        False    False          False          False    False  False                     False  False    False
560        False    False          False          False    False  False                     False  False    False
561        False    False          False          False    False  False                     False  False    False
562        False    False          False          False    False  False                     False  False    False
563        False    False          False          False    False  False                     False  False    False
564        False    False          False          False    False  False                     False  False    False
565        False    False          False          False    False  False                     False  False    False
566        False    False          False          False    False  False                     False  False    False
567        False    False          False          False    False  False                     False  False    False
568        False    False          False          False    False  False                     False  False    False
569        False    False          False          False    False  False                     False  False    False
570        False    False          False          False    False  False                     False  False    False
571        False    False          False          False    False  False                     False  False    False
572        False    False          False          False    False  False                     False  False    False
573        False    False          False          False    False  False                     False  False    False
574        False    False          False          False    False  False                     False  False    False
575        False    False          False          False    False  False                     False  False    False
576        False    False          False          False    False  False                     False  False    False
577        False    False          False          False    False  False                     False  False    False
578        False    False          False          False    False  False                     False  False    False
579        False    False          False          False    False  False                     False  False    False
580        False    False          False          False    False  False                     False  False    False
581        False    False          False          False    False  False                     False  False    False
582        False    False          False          False    False  False                     False  False    False
583        False    False          False          False    False  False                     False  False    False
584        False    False          False          False    False  False                     False  False    False
585        False    False          False          False    False  False                     False  False    False
586        False    False          False          False    False  False                     False  False    False
587        False    False          False          False    False  False                     False  False    False
588        False    False          False          False    False  False                     False  False    False
589        False    False          False          False    False  False                     False  False    False
590        False    False          False          False    False  False                     False  False    False
591        False    False          False          False    False  False                     False  False    False
592        False    False          False          False    False  False                     False  False    False
593        False    False          False          False    False  False                     False  False    False
594        False    False          False          False    False  False                     False  False    False
595        False    False          False          False    False  False                     False  False    False
596        False    False          False          False    False  False                     False  False    False
597        False    False          False          False    False  False                     False  False    False
598        False    False          False          False    False  False                     False  False    False
599        False    False          False          False    False  False                     False  False    False
600        False    False          False          False    False  False                     False  False    False
601        False    False          False          False    False  False                     False  False    False
602        False    False          False          False    False  False                     False  False    False
603        False    False          False          False    False  False                     False  False    False
604        False    False          False          False    False  False                     False  False    False
605        False    False          False          False    False  False                     False  False    False
606        False    False          False          False    False  False                     False  False    False
607        False    False          False          False    False  False                     False  False    False
608        False    False          False          False    False  False                     False  False    False
609        False    False          False          False    False  False                     False  False    False
610        False    False          False          False    False  False                     False  False    False
611        False    False          False          False    False  False                     False  False    False
612        False    False          False          False    False  False                     False  False    False
613        False    False          False          False    False  False                     False  False    False
614        False    False          False          False    False  False                     False  False    False
615        False    False          False          False    False  False                     False  False    False
616        False    False          False          False    False  False                     False  False    False
617        False    False          False          False    False  False                     False  False    False
618        False    False          False          False    False  False                     False  False    False
619        False    False          False          False    False  False                     False  False    False
620        False    False          False          False    False  False                     False  False    False
621        False    False          False          False    False  False                     False  False    False
622        False    False          False          False    False  False                     False  False    False
623        False    False          False          False    False  False                     False  False    False
624        False    False          False          False    False  False                     False  False    False
625        False    False          False          False    False  False                     False  False    False
626        False    False          False          False    False  False                     False  False    False
627        False    False          False          False    False  False                     False  False    False
628        False    False          False          False    False  False                     False  False    False
629        False    False          False          False    False  False                     False  False    False
630        False    False          False          False    False  False                     False  False    False
631        False    False          False          False    False  False                     False  False    False
632        False    False          False          False    False  False                     False  False    False
633        False    False          False          False    False  False                     False  False    False
634        False    False          False          False    False  False                     False  False    False
635        False    False          False          False    False  False                     False  False    False
636        False    False          False          False    False  False                     False  False    False
637        False    False          False          False    False  False                     False  False    False
638        False    False          False          False    False  False                     False  False    False
639        False    False          False          False    False  False                     False  False    False
640        False    False          False          False    False  False                     False  False    False
641        False    False          False          False    False  False                     False  False    False
642        False    False          False          False    False  False                     False  False    False
643        False    False          False          False    False  False                     False  False    False
644        False    False          False          False    False  False                     False  False    False
645        False    False          False          False    False  False                     False  False    False
646        False    False          False          False    False  False                     False  False    False
647        False    False          False          False    False  False                     False  False    False
648        False    False          False          False    False  False                     False  False    False
649        False    False          False          False    False  False                     False  False    False
650        False    False          False          False    False  False                     False  False    False
651        False    False          False          False    False  False                     False  False    False
652        False    False          False          False    False  False                     False  False    False
653        False    False          False          False    False  False                     False  False    False
654        False    False          False          False    False  False                     False  False    False
655        False    False          False          False    False  False                     False  False    False
656        False    False          False          False    False  False                     False  False    False
657        False    False          False          False    False  False                     False  False    False
658        False    False          False          False    False  False                     False  False    False
659        False    False          False          False    False  False                     False  False    False
660        False    False          False          False    False  False                     False  False    False
661        False    False          False          False    False  False                     False  False    False
662        False    False          False          False    False  False                     False  False    False
663        False    False          False          False    False  False                     False  False    False
664        False    False          False          False    False  False                     False  False    False
665        False    False          False          False    False  False                     False  False    False
666        False    False          False          False    False  False                     False  False    False
667        False    False          False          False    False  False                     False  False    False
668        False    False          False          False    False  False                     False  False    False
669        False    False          False          False    False  False                     False  False    False
670        False    False          False          False    False  False                     False  False    False
671        False    False          False          False    False  False                     False  False    False
672        False    False          False          False    False  False                     False  False    False
673        False    False          False          False    False  False                     False  False    False
674        False    False          False          False    False  False                     False  False    False
675        False    False          False          False    False  False                     False  False    False
676        False    False          False          False    False  False                     False  False    False
677        False    False          False          False    False  False                     False  False    False
678        False    False          False          False    False  False                     False  False    False
679        False    False          False          False    False  False                     False  False    False
680        False    False          False          False    False  False                     False  False    False
681        False    False          False          False    False  False                     False  False    False
682        False    False          False          False    False  False                     False  False    False
683        False    False          False          False    False  False                     False  False    False
684        False    False          False          False    False  False                     False  False    False
685        False    False          False          False    False  False                     False  False    False
686        False    False          False          False    False  False                     False  False    False
687        False    False          False          False    False  False                     False  False    False
688        False    False          False          False    False  False                     False  False    False
689        False    False          False          False    False  False                     False  False    False
690        False    False          False          False    False  False                     False  False    False
691        False    False          False          False    False  False                     False  False    False
692        False    False          False          False    False  False                     False  False    False
693        False    False          False          False    False  False                     False  False    False
694        False    False          False          False    False  False                     False  False    False
695        False    False          False          False    False  False                     False  False    False
696        False    False          False          False    False  False                     False  False    False
697        False    False          False          False    False  False                     False  False    False
698        False    False          False          False    False  False                     False  False    False
699        False    False          False          False    False  False                     False  False    False
700        False    False          False          False    False  False                     False  False    False
701        False    False          False          False    False  False                     False  False    False
702        False    False          False          False    False  False                     False  False    False
703        False    False          False          False    False  False                     False  False    False
704        False    False          False          False    False  False                     False  False    False
705        False    False          False          False    False  False                     False  False    False
706        False    False          False          False    False  False                     False  False    False
707        False    False          False          False    False  False                     False  False    False
708        False    False          False          False    False  False                     False  False    False
709        False    False          False          False    False  False                     False  False    False
710        False    False          False          False    False  False                     False  False    False
711        False    False          False          False    False  False                     False  False    False
712        False    False          False          False    False  False                     False  False    False
713        False    False          False          False    False  False                     False  False    False
714        False    False          False          False    False  False                     False  False    False
715        False    False          False          False    False  False                     False  False    False
716        False    False          False          False    False  False                     False  False    False
717        False    False          False          False    False  False                     False  False    False
718        False    False          False          False    False  False                     False  False    False
719        False    False          False          False    False  False                     False  False    False
720        False    False          False          False    False  False                     False  False    False
721        False    False          False          False    False  False                     False  False    False
722        False    False          False          False    False  False                     False  False    False
723        False    False          False          False    False  False                     False  False    False
724        False    False          False          False    False  False                     False  False    False
725        False    False          False          False    False  False                     False  False    False
726        False    False          False          False    False  False                     False  False    False
727        False    False          False          False    False  False                     False  False    False
728        False    False          False          False    False  False                     False  False    False
729        False    False          False          False    False  False                     False  False    False
730        False    False          False          False    False  False                     False  False    False
731        False    False          False          False    False  False                     False  False    False
732        False    False          False          False    False  False                     False  False    False
733        False    False          False          False    False  False                     False  False    False
734        False    False          False          False    False  False                     False  False    False
735        False    False          False          False    False  False                     False  False    False
736        False    False          False          False    False  False                     False  False    False
737        False    False          False          False    False  False                     False  False    False
738        False    False          False          False    False  False                     False  False    False
739        False    False          False          False    False  False                     False  False    False
740        False    False          False          False    False  False                     False  False    False
741        False    False          False          False    False  False                     False  False    False
742        False    False          False          False    False  False                     False  False    False
743        False    False          False          False    False  False                     False  False    False
744        False    False          False          False    False  False                     False  False    False
745        False    False          False          False    False  False                     False  False    False
746        False    False          False          False    False  False                     False  False    False
747        False    False          False          False    False  False                     False  False    False
748        False    False          False          False    False  False                     False  False    False
749        False    False          False          False    False  False                     False  False    False
750        False    False          False          False    False  False                     False  False    False
751        False    False          False          False    False  False                     False  False    False
752        False    False          False          False    False  False                     False  False    False
753        False    False          False          False    False  False                     False  False    False
754        False    False          False          False    False  False                     False  False    False
755        False    False          False          False    False  False                     False  False    False
756        False    False          False          False    False  False                     False  False    False
757        False    False          False          False    False  False                     False  False    False
758        False    False          False          False    False  False                     False  False    False
759        False    False          False          False    False  False                     False  False    False
760        False    False          False          False    False  False                     False  False    False
761        False    False          False          False    False  False                     False  False    False
762        False    False          False          False    False  False                     False  False    False
763        False    False          False          False    False  False                     False  False    False
764        False    False          False          False    False  False                     False  False    False
765        False    False          False          False    False  False                     False  False    False
766        False    False          False          False    False  False                     False  False    False
767        False    False          False          False    False  False                     False  False    False
>>> 
>>> 
>>> res=pd.read_csv("C://python37//Prog//files//Employee.csv")
>>> pd.isnull(res)
       eid  fname  lname  email  phone  hiredate  jobid  salary   comm    mid    did
0    False  False  False  False  False     False  False   False   True   True  False
1    False  False  False  False  False     False  False   False   True  False  False
2    False  False  False  False  False     False  False   False   True  False  False
3    False  False  False  False  False     False  False   False   True  False  False
4    False  False  False  False  False     False  False   False   True  False  False
5    False  False  False  False  False     False  False   False   True  False  False
6    False  False  False  False  False     False  False   False   True  False  False
7    False  False  False  False  False     False  False   False   True  False  False
8    False  False  False  False  False     False  False   False   True  False  False
9    False  False  False  False  False     False  False   False   True  False  False
10   False  False  False  False  False     False  False   False   True  False  False
11   False  False  False  False  False     False  False   False   True  False  False
12   False  False  False  False  False     False  False   False   True  False  False
13   False  False  False  False  False     False  False   False   True  False  False
14   False  False  False  False  False     False  False   False   True  False  False
15   False  False  False  False  False     False  False   False   True  False  False
16   False  False  False  False  False     False  False   False   True  False  False
17   False  False  False  False  False     False  False   False   True  False  False
18   False  False  False  False  False     False  False   False   True  False  False
19   False  False  False  False  False     False  False   False   True  False  False
20   False  False  False  False  False     False  False   False   True  False  False
21   False  False  False  False  False     False  False   False   True  False  False
22   False  False  False  False  False     False  False   False   True  False  False
23   False  False  False  False  False     False  False   False   True  False  False
24   False  False  False  False  False     False  False   False   True  False  False
25   False  False  False  False  False     False  False   False   True  False  False
26   False  False  False  False  False     False  False   False   True  False  False
27   False  False  False  False  False     False  False   False   True  False  False
28   False  False  False  False  False     False  False   False   True  False  False
29   False  False  False  False  False     False  False   False   True  False  False
30   False  False  False  False  False     False  False   False   True  False  False
31   False  False  False  False  False     False  False   False   True  False  False
32   False  False  False  False  False     False  False   False   True  False  False
33   False  False  False  False  False     False  False   False   True  False  False
34   False  False  False  False  False     False  False   False   True  False  False
35   False  False  False  False  False     False  False   False   True  False  False
36   False  False  False  False  False     False  False   False   True  False  False
37   False  False  False  False  False     False  False   False   True  False  False
38   False  False  False  False  False     False  False   False   True  False  False
39   False  False  False  False  False     False  False   False   True  False  False
40   False  False  False  False  False     False  False   False   True  False  False
41   False  False  False  False  False     False  False   False   True  False  False
42   False  False  False  False  False     False  False   False   True  False  False
43   False  False  False  False  False     False  False   False   True  False  False
44   False  False  False  False  False     False  False   False   True  False  False
45   False  False  False  False  False     False  False   False  False  False  False
46   False  False  False  False  False     False  False   False  False  False  False
47   False  False  False  False  False     False  False   False  False  False  False
48   False  False  False  False  False     False  False   False  False  False  False
49   False  False  False  False  False     False  False   False  False  False  False
50   False  False  False  False  False     False  False   False  False  False  False
51   False  False  False  False  False     False  False   False  False  False  False
52   False  False  False  False  False     False  False   False  False  False  False
53   False  False  False  False  False     False  False   False  False  False  False
54   False  False  False  False  False     False  False   False  False  False  False
55   False  False  False  False  False     False  False   False  False  False  False
56   False  False  False  False  False     False  False   False  False  False  False
57   False  False  False  False  False     False  False   False  False  False  False
58   False  False  False  False  False     False  False   False  False  False  False
59   False  False  False  False  False     False  False   False  False  False  False
60   False  False  False  False  False     False  False   False  False  False  False
61   False  False  False  False  False     False  False   False  False  False  False
62   False  False  False  False  False     False  False   False  False  False  False
63   False  False  False  False  False     False  False   False  False  False  False
64   False  False  False  False  False     False  False   False  False  False  False
65   False  False  False  False  False     False  False   False  False  False  False
66   False  False  False  False  False     False  False   False  False  False  False
67   False  False  False  False  False     False  False   False  False  False  False
68   False  False  False  False  False     False  False   False  False  False  False
69   False  False  False  False  False     False  False   False  False  False  False
70   False  False  False  False  False     False  False   False  False  False  False
71   False  False  False  False  False     False  False   False  False  False  False
72   False  False  False  False  False     False  False   False  False  False  False
73   False  False  False  False  False     False  False   False  False  False  False
74   False  False  False  False  False     False  False   False  False  False  False
75   False  False  False  False  False     False  False   False  False  False  False
76   False  False  False  False  False     False  False   False  False  False  False
77   False  False  False  False  False     False  False   False  False  False  False
78   False  False  False  False  False     False  False   False  False  False   True
79   False  False  False  False  False     False  False   False  False  False  False
80   False  False  False  False  False     False  False   False   True  False  False
81   False  False  False  False  False     False  False   False   True  False  False
82   False  False  False  False  False     False  False   False   True  False  False
83   False  False  False  False  False     False  False   False   True  False  False
84   False  False  False  False  False     False  False   False   True  False  False
85   False  False  False  False  False     False  False   False   True  False  False
86   False  False  False  False  False     False  False   False   True  False  False
87   False  False  False  False  False     False  False   False   True  False  False
88   False  False  False  False  False     False  False   False   True  False  False
89   False  False  False  False  False     False  False   False   True  False  False
90   False  False  False  False  False     False  False   False   True  False  False
91   False  False  False  False  False     False  False   False   True  False  False
92   False  False  False  False  False     False  False   False   True  False  False
93   False  False  False  False  False     False  False   False   True  False  False
94   False  False  False  False  False     False  False   False   True  False  False
95   False  False  False  False  False     False  False   False   True  False  False
96   False  False  False  False  False     False  False   False   True  False  False
97   False  False  False  False  False     False  False   False   True  False  False
98   False  False  False  False  False     False  False   False   True  False  False
99   False  False  False  False  False     False  False   False   True  False  False
100  False  False  False  False  False     False  False   False   True  False  False
>>> 
>>> #For replace null values with 0
>>> 
>>> res.fillna(0)
     eid        fname        lname               email               phone     hiredate       jobid  salary  comm    mid    did
0    100       Steven         King     sking@gmail.com        515.123.4567  17-06-1987      AD_PRES   24000  0.00    0.0   90.0
1    101        Neena      Kochhar  nkochhar@gmail.com        515.123.4568  21-09-1989        AD_VP   17000  0.00  100.0   90.0
2    102          Lex      De Haan   ldehaan@gmail.com        515.123.4569  13-01-1993        AD_VP   17000  0.00  100.0   90.0
3    103    Alexander       Hunold   ahunold@gmail.com        590.423.4567  03-01-1990      IT_PROG    9000  0.00  102.0   60.0
4    104        Bruce        Ernst    bernst@gmail.com        590.423.4568  21-05-1991      IT_PROG    6000  0.00  103.0   60.0
5    105        David       Austin   daustin@gmail.com        590.423.4569  25-06-1997      IT_PROG    4800  0.00  103.0   60.0
6    106        Valli    Pataballa  vpatabal@gmail.com        590.423.4560  05-02-1998      IT_PROG    4800  0.00  103.0   60.0
7    107        Diana      Lorentz  dlorentz@gmail.com        590.423.5567  07-02-1999      IT_PROG    4200  0.00  103.0   60.0
8    108        Nancy    Greenberg  ngreenbe@gmail.com        515.124.4569  17-08-1994       FI_MGR   12000  0.00  101.0  100.0
9    109       Daniel       Faviet   dfaviet@gmail.com        515.124.4169  16-08-1994   FI_ACCOUNT    9000  0.00  108.0  100.0
10   110         John         Chen     jchen@gmail.com        515.124.4269  28-09-1997   FI_ACCOUNT    8200  0.00  108.0  100.0
11   111       Ismael      Sciarra  isciarra@gmail.com        515.124.4369  30-09-1997   FI_ACCOUNT    7700  0.00  108.0  100.0
12   112  Jose Manuel        Urman   jmurman@gmail.com        515.124.4469  07-03-1998   FI_ACCOUNT    7800  0.00  108.0  100.0
13   113         Luis         Popp     lpopp@gmail.com        515.124.4567  07-12-1999   FI_ACCOUNT    6900  0.00  108.0  100.0
14   114          Den     Raphaely  drapheal@gmail.com        515.127.4561  07-12-1994       PU_MAN   11000  0.00  100.0   30.0
15   115    Alexander         Khoo   akhoo@gmail.co.in        515.127.4562  18-05-1995     PU_CLERK    3100  0.00  114.0   30.0
16   116       Shelli        Baida    sbaida@gmail.com        515.127.4563  24-12-1997     PU_CLERK    2900  0.00  114.0   30.0
17   117        Sigal       Tobias   stobias@gmail.com        515.127.4564  24-07-1997     PU_CLERK    2800  0.00  114.0   30.0
18   118          Guy       Himuro   ghimuro@gmail.com        515.127.4565  15-11-1998     PU_CLERK    2600  0.00  114.0   30.0
19   119        Karen   Colmenares  kcolmena@gmail.com        515.127.4566  10-08-1999     PU_CLERK    2500  0.00  114.0   30.0
20   120      Matthew        Weiss    mweiss@gmail.com        650.123.1234  18-07-1996       ST_MAN    8000  0.00  100.0   50.0
21   121         Adam        Fripp    afripp@gmail.com        650.123.2234  10-04-1997       ST_MAN    8200  0.00  100.0   50.0
22   122        Payam     Kaufling  pkauflin@gmail.com        650.123.3234  01-05-1995       ST_MAN    7900  0.00  100.0   50.0
23   123       Shanta      Vollman  svollman@gmail.com        650.123.4234  10-10-1997       ST_MAN    6500  0.00  100.0   50.0
24   124        Kevin      Mourgos  kmourgos@gmail.com        650.123.5234  16-11-1999       ST_MAN    5800  0.00  100.0   50.0
25   125        Julia        Nayer    jnayer@gmail.com        650.124.1214  16-07-1997     ST_CLERK    3200  0.00  120.0   50.0
26   126        Irene  Mikkilineni  imikkili@gmail.com        650.124.1224  28-09-1998     ST_CLERK    2700  0.00  120.0   50.0
27   127        James       Landry   jlandry@gmail.com        650.124.1334  14-01-1999     ST_CLERK    2400  0.00  120.0   50.0
28   128       Steven       Markle   smarkle@gmail.com        650.124.1434  08-03-2000     ST_CLERK    2200  0.00  120.0   50.0
29   129        Laura       Bissot   lbissot@gmail.com        650.124.5234  20-08-1997     ST_CLERK    3300  0.00  121.0   50.0
30   130        Mozhe     Atkinson  matkinso@gmail.com        650.124.6234  30-10-1997     ST_CLERK    2800  0.00  121.0   50.0
31   131        James       Marlow   jamrlow@gmail.com        650.124.7234  16-02-1997     ST_CLERK    2500  0.00  121.0   50.0
32   132           TJ        Olson   tjolson@gmail.com        650.124.8234  10-04-1999     ST_CLERK    2100  0.00  121.0   50.0
33   133        Jason       Mallin   jmallin@gmail.com        650.127.1934  14-06-1996     ST_CLERK    3300  0.00  122.0   50.0
34   134      Michael       Rogers   mrogers@gmail.com        650.127.1834  26-08-1998     ST_CLERK    2900  0.00  122.0   50.0
35   135           Ki          Gee      kgee@gmail.com        650.127.1734  12-12-1999     ST_CLERK    2400  0.00  122.0   50.0
36   136        Hazel   Philtanker  hphiltan@gmail.com        650.127.1634  06-02-2000     ST_CLERK    2200  0.00  122.0   50.0
37   137       Renske       Ladwig   rladwig@gmail.com        650.121.1234  14-07-1995     ST_CLERK    3600  0.00  123.0   50.0
38   138      Stephen       Stiles   sstiles@gmail.com        650.121.2034  26-10-1997     ST_CLERK    3200  0.00  123.0   50.0
39   139         John          Seo      jseo@gmail.com        650.121.2019  12-02-1998     ST_CLERK    2700  0.00  123.0   50.0
40   140       Joshua        Patel    jpatel@gmail.com        650.121.1834  06-04-1998     ST_CLERK    2500  0.00  123.0   20.0
41   141       Trenna         Rajs     trajs@gmail.com        650.121.8009  17-10-1995     ST_CLERK    3500  0.00  124.0   20.0
42   142       Curtis       Davies   cdavies@gmail.com        650.121.2994  29-01-1997     ST_CLERK    3100  0.00  124.0   50.0
43   143      Randall        Matos    rmatos@gmail.com        650.121.2874  15-03-1998     ST_CLERK    2600  0.00  124.0   50.0
44   144        Peter       Vargas   pvargas@gmail.com        650.121.2004  09-07-1998     ST_CLERK    2500  0.00  124.0   50.0
45   145         John      Russell   jrussel@gmail.com  011.44.1344.429268  01-10-1996       SA_MAN   14000  0.40  100.0   80.0
46   146        Karen     Partners  kpartner@gmail.com  011.44.1344.467268  05-01-1997       SA_MAN   13500  0.30  100.0   80.0
47   147      Alberto    Errazuriz  aerrazur@gmail.com  011.44.1344.429278  10-03-1997       SA_MAN   12000  0.30  100.0   80.0
48   148       Gerald    Cambrault  gcambrau@gmail.com  011.44.1344.619268  15-10-1999       SA_MAN   11000  0.30  100.0   80.0
49   149        Eleni      Zlotkey  ezlotkey@gmail.com  011.44.1344.429018  29-01-2000       SA_MAN   10500  0.20  100.0   80.0
50   150        Peter       Tucker   ptucker@gmail.com  011.44.1344.129268  30-01-1997       SA_REP   10000  0.30  145.0   80.0
51   151        David    Bernstein  dbernste@gmail.com  011.44.1344.345268  24-03-1997       SA_REP    9500  0.25  145.0   80.0
52   152        Peter         Hall     phall@gmail.com  011.44.1344.478968  20-08-1997       SA_REP    9000  0.25  145.0   80.0
53   153  Christopher        Olsen    colsen@gmail.com  011.44.1344.498718  30-03-1998       SA_REP    8000  0.20  145.0   80.0
54   154      Nanette    Cambrault  ncambrau@gmail.com  011.44.1344.987668  09-12-1998       SA_REP    7500  0.20  145.0   80.0
55   155       Oliver      Tuvault  otuvault@gmail.com  011.44.1344.486508  23-11-1999       SA_REP    7000  0.15  145.0   80.0
56   156      Janette         King     jking@gmail.com  011.44.1345.429268  30-01-1996       SA_REP   10000  0.35  146.0   80.0
57   157      Patrick        Sully    psully@gmail.com  011.44.1345.929268  04-03-1996       SA_REP    9500  0.35  146.0   80.0
58   158        Allan       McEwen   amcewen@gmail.com  011.44.1345.829268  01-08-1996       SA_REP    9000  0.35  146.0   80.0
59   159      Lindsey        Smith    lsmith@gmail.com  011.44.1345.729268  10-03-1997       SA_REP    8000  0.30  146.0   80.0
60   160       Louise        Doran    ldoran@gmail.com  011.44.1345.629268  15-12-1997       SA_REP    7500  0.30  146.0   80.0
61   161       Sarath       Sewall   ssewall@gmail.com  011.44.1345.529268  03-11-1998       SA_REP    7000  0.25  146.0   80.0
62   162        Clara      Vishney  cvishney@gmail.com  011.44.1346.129268  11-11-1997       SA_REP   10500  0.25  147.0   80.0
63   163     Danielle       Greene   dgreene@gmail.com  011.44.1346.229268  19-03-1999       SA_REP    9500  0.15  147.0   80.0
64   164       Mattea      Marvins  mmarvins@gmail.com  011.44.1346.329268  24-01-2000       SA_REP    7200  0.10  147.0   80.0
65   165        David          Lee      dlee@gmail.com  011.44.1346.529268  23-02-2000       SA_REP    6800  0.10  147.0   80.0
66   166       Sundar         Ande     sande@gmail.com  011.44.1346.629268  24-03-2000       SA_REP    6400  0.10  147.0   80.0
67   167         Amit        Banda    abanda@gmail.com  011.44.1346.729268  21-04-2000       SA_REP    6200  0.10  147.0   80.0
68   168         Lisa         Ozer     lozer@gmail.com  011.44.1343.929268  11-03-1997       SA_REP   11500  0.25  148.0   80.0
69   169     Harrison        Bloom    hbloom@gmail.com  011.44.1343.829268  23-03-1998       SA_REP   10000  0.20  148.0   80.0
70   170       Tayler          Fox      tfox@gmail.com  011.44.1343.729268  24-01-1998       SA_REP    9600  0.20  148.0   80.0
71   171      William        Smith    wsmith@gmail.com  011.44.1343.629268  23-02-1999       SA_REP    7400  0.15  148.0   80.0
72   172    Elizabeth        Bates    ebates@gmail.com  011.44.1343.529268  24-03-1999       SA_REP    7300  0.15  148.0   80.0
73   173      Sundita        Kumar    skumar@gmail.com  011.44.1343.329268  21-04-2000       SA_REP    6100  0.10  148.0   80.0
74   174        Ellen         Abel     eabel@gmail.com  011.44.1644.429267  11-05-1996       SA_REP   11000  0.30  149.0   80.0
75   175       Alyssa       Hutton   ahutton@gmail.com  011.44.1644.429266  19-03-1997       SA_REP    8800  0.25  149.0   80.0
76   176     Jonathon       Taylor   jtaylor@gmail.com  011.44.1644.429265  24-03-1998       SA_REP    8600  0.20  149.0   80.0
77   177         Jack   Livingston  jlivings@gmail.com  011.44.1644.429264  23-04-1998       SA_REP    8400  0.20  149.0   80.0
78   178    Kimberely        Grant    kgrant@gmail.com  011.44.1644.429263  24-05-1999       SA_REP    7000  0.15  149.0    0.0
79   179      Charles      Johnson  cjohnson@gmail.com  011.44.1644.429262  04-01-2000       SA_REP    6200  0.10  149.0   80.0
80   180      Winston       Taylor   wtaylor@gmail.com        650.507.9876  24-01-1998     SH_CLERK    3200  0.00  120.0   50.0
81   181         Jean       Fleaur   jfleaur@gmail.com        650.507.9877  23-02-1998     SH_CLERK    3100  0.00  120.0   50.0
82   182       Martha     Sullivan  msulliva@gmail.com        650.507.9878  21-06-1999     SH_CLERK    2500  0.00  120.0   50.0
83   183       Girard        Geoni    ggeoni@gmail.com        650.507.9879  03-02-2000     SH_CLERK    2800  0.00  120.0   50.0
84   184      Nandita     Sarchand  nsarchan@gmail.com        650.509.1876  27-01-1996     SH_CLERK    4200  0.00  121.0   50.0
85   185       Alexis         Bull     abull@gmail.com        650.509.2876  20-02-1997     SH_CLERK    4100  0.00  121.0   50.0
86   186        Julia    Dellinger  jdelling@gmail.com        650.509.3876  24-06-1998     SH_CLERK    3400  0.00  121.0   50.0
87   187      Anthony       Cabrio   acabrio@gmail.com        650.509.4876  07-02-1999     SH_CLERK    3000  0.00  121.0   50.0
88   188        Kelly        Chung    kchung@gmail.com        650.505.1876  14-06-1997     SH_CLERK    3800  0.00  122.0   50.0
89   189     Jennifer        Dilly    jdilly@gmail.com        650.505.2876  13-08-1997     SH_CLERK    3600  0.00  122.0   50.0
90   190      Timothy        Gates    tgates@gmail.com        650.505.3876  11-07-1998     SH_CLERK    2900  0.00  122.0   50.0
91   191      Randall      Perkins  rperkins@gmail.com        650.505.4876  19-12-1999     SH_CLERK    2500  0.00  122.0   50.0
92   192        Sarah         Bell     sbell@gmail.com        650.501.1876  04-02-1996     SH_CLERK    4000  0.00  123.0   50.0
93   193      Britney      Everett  beverett@gmail.com        650.501.2876  03-03-1997     SH_CLERK    3900  0.00  123.0   50.0
94   194       Samuel       McCain   smccain@gmail.com        650.501.3876  01-07-1998     SH_CLERK    3200  0.00  123.0   40.0
95   195        Vance        Jones    vjones@gmail.com        650.501.4876  17-03-1999     SH_CLERK    2800  0.00  123.0   40.0
96   196        Alana        Walsh    awalsh@gmail.com        650.507.9811  24-04-1998     SH_CLERK    3100  0.00  124.0   40.0
97   197        Kevin       Feeney   kfeeney@gmail.com        650.507.9822  23-05-1998     SH_CLERK    3000  0.00  124.0   40.0
98   198       Donald     OConnell  doconnel@gmail.com        650.507.9833  21-06-1999     SH_CLERK    2600  0.00  124.0   50.0
99   199      Douglas        Grant    dgrant@gmail.com        650.507.9844  13-01-2000     SH_CLERK    2600  0.00  124.0   50.0
100  200     Jennifer       Whalen   jwhalen@gmail.com        515.123.4444  17-09-1987      AD_ASST    4400  0.00  101.0   10.0
>>> 

>>> 
>>> 
>>> res.head(10)
   eid      fname      lname               email         phone     hiredate       jobid  salary  comm    mid    did
0  100     Steven       King     sking@gmail.com  515.123.4567  17-06-1987      AD_PRES   24000   NaN    NaN   90.0
1  101      Neena    Kochhar  nkochhar@gmail.com  515.123.4568  21-09-1989        AD_VP   17000   NaN  100.0   90.0
2  102        Lex    De Haan   ldehaan@gmail.com  515.123.4569  13-01-1993        AD_VP   17000   NaN  100.0   90.0
3  103  Alexander     Hunold   ahunold@gmail.com  590.423.4567  03-01-1990      IT_PROG    9000   NaN  102.0   60.0
4  104      Bruce      Ernst    bernst@gmail.com  590.423.4568  21-05-1991      IT_PROG    6000   NaN  103.0   60.0
5  105      David     Austin   daustin@gmail.com  590.423.4569  25-06-1997      IT_PROG    4800   NaN  103.0   60.0
6  106      Valli  Pataballa  vpatabal@gmail.com  590.423.4560  05-02-1998      IT_PROG    4800   NaN  103.0   60.0
7  107      Diana    Lorentz  dlorentz@gmail.com  590.423.5567  07-02-1999      IT_PROG    4200   NaN  103.0   60.0
8  108      Nancy  Greenberg  ngreenbe@gmail.com  515.124.4569  17-08-1994       FI_MGR   12000   NaN  101.0  100.0
9  109     Daniel     Faviet   dfaviet@gmail.com  515.124.4169  16-08-1994   FI_ACCOUNT    9000   NaN  108.0  100.0
>>> res.tail(3)
     eid     fname     lname               email         phone     hiredate     jobid  salary  comm    mid   did
98   198    Donald  OConnell  doconnel@gmail.com  650.507.9833  21-06-1999   SH_CLERK    2600   NaN  124.0  50.0
99   199   Douglas     Grant    dgrant@gmail.com  650.507.9844  13-01-2000   SH_CLERK    2600   NaN  124.0  50.0
100  200  Jennifer    Whalen   jwhalen@gmail.com  515.123.4444  17-09-1987    AD_ASST    4400   NaN  101.0  10.0
>>> 
>>> res.dtypes
eid           int64
fname        object
lname        object
email        object
phone        object
hiredate     object
jobid        object
salary        int64
comm        float64
mid         float64
did         float64
dtype: object
>>> 
>>> res.columns
Index(['eid', 'fname', 'lname', 'email', 'phone', 'hiredate', 'jobid', 'salary', 'comm', 'mid', 'did'], dtype='object')
>>> res['fname'].unique()
array(['Steven', 'Neena', 'Lex', 'Alexander', 'Bruce', 'David', 'Valli',
       'Diana', 'Nancy', 'Daniel', 'John', 'Ismael', 'Jose Manuel',
       'Luis', 'Den', 'Shelli', 'Sigal', 'Guy', 'Karen', 'Matthew',
       'Adam', 'Payam', 'Shanta', 'Kevin', 'Julia', 'Irene', 'James',
       'Laura', 'Mozhe', 'TJ', 'Jason', 'Michael', 'Ki', 'Hazel',
       'Renske', 'Stephen', 'Joshua', 'Trenna', 'Curtis', 'Randall',
       'Peter', 'Alberto', 'Gerald', 'Eleni', 'Christopher', 'Nanette',
       'Oliver', 'Janette', 'Patrick', 'Allan', 'Lindsey', 'Louise',
       'Sarath', 'Clara', 'Danielle', 'Mattea', 'Sundar', 'Amit', 'Lisa',
       'Harrison', 'Tayler', 'William', 'Elizabeth', 'Sundita', 'Ellen',
       'Alyssa', 'Jonathon', 'Jack', 'Kimberely', 'Charles', 'Winston',
       'Jean', 'Martha', 'Girard', 'Nandita', 'Alexis', 'Anthony',
       'Kelly', 'Jennifer', 'Timothy', 'Sarah', 'Britney', 'Samuel',
       'Vance', 'Alana', 'Donald', 'Douglas'], dtype=object)
>>> res.duplicated()
0      False
1      False
2      False
3      False
4      False
5      False
6      False
7      False
8      False
9      False
10     False
11     False
12     False
13     False
14     False
15     False
16     False
17     False
18     False
19     False
20     False
21     False
22     False
23     False
24     False
25     False
26     False
27     False
28     False
29     False
30     False
31     False
32     False
33     False
34     False
35     False
36     False
37     False
38     False
39     False
40     False
41     False
42     False
43     False
44     False
45     False
46     False
47     False
48     False
49     False
50     False
51     False
52     False
53     False
54     False
55     False
56     False
57     False
58     False
59     False
60     False
61     False
62     False
63     False
64     False
65     False
66     False
67     False
68     False
69     False
70     False
71     False
72     False
73     False
74     False
75     False
76     False
77     False
78     False
79     False
80     False
81     False
82     False
83     False
84     False
85     False
86     False
87     False
88     False
89     False
90     False
91     False
92     False
93     False
94     False
95     False
96     False
97     False
98     False
99     False
100    False
dtype: bool
>>> 
>>> 
>>> res.values
array([[100, 'Steven', 'King', ..., nan, nan, 90.0],
       [101, 'Neena', 'Kochhar', ..., nan, 100.0, 90.0],
       [102, 'Lex', 'De Haan', ..., nan, 100.0, 90.0],
       ...,
       [198, 'Donald', 'OConnell', ..., nan, 124.0, 50.0],
       [199, 'Douglas', 'Grant', ..., nan, 124.0, 50.0],
       [200, 'Jennifer', 'Whalen', ..., nan, 101.0, 10.0]], dtype=object)
>>> 
>>> res.sort_values(by='fname',ascending=True)
     eid        fname        lname               email               phone     hiredate       jobid  salary  comm    mid    did
21   121         Adam        Fripp    afripp@gmail.com        650.123.2234  10-04-1997       ST_MAN    8200   NaN  100.0   50.0
96   196        Alana        Walsh    awalsh@gmail.com        650.507.9811  24-04-1998     SH_CLERK    3100   NaN  124.0   40.0
47   147      Alberto    Errazuriz  aerrazur@gmail.com  011.44.1344.429278  10-03-1997       SA_MAN   12000  0.30  100.0   80.0
3    103    Alexander       Hunold   ahunold@gmail.com        590.423.4567  03-01-1990      IT_PROG    9000   NaN  102.0   60.0
15   115    Alexander         Khoo   akhoo@gmail.co.in        515.127.4562  18-05-1995     PU_CLERK    3100   NaN  114.0   30.0
85   185       Alexis         Bull     abull@gmail.com        650.509.2876  20-02-1997     SH_CLERK    4100   NaN  121.0   50.0
58   158        Allan       McEwen   amcewen@gmail.com  011.44.1345.829268  01-08-1996       SA_REP    9000  0.35  146.0   80.0
75   175       Alyssa       Hutton   ahutton@gmail.com  011.44.1644.429266  19-03-1997       SA_REP    8800  0.25  149.0   80.0
67   167         Amit        Banda    abanda@gmail.com  011.44.1346.729268  21-04-2000       SA_REP    6200  0.10  147.0   80.0
87   187      Anthony       Cabrio   acabrio@gmail.com        650.509.4876  07-02-1999     SH_CLERK    3000   NaN  121.0   50.0
93   193      Britney      Everett  beverett@gmail.com        650.501.2876  03-03-1997     SH_CLERK    3900   NaN  123.0   50.0
4    104        Bruce        Ernst    bernst@gmail.com        590.423.4568  21-05-1991      IT_PROG    6000   NaN  103.0   60.0
79   179      Charles      Johnson  cjohnson@gmail.com  011.44.1644.429262  04-01-2000       SA_REP    6200  0.10  149.0   80.0
53   153  Christopher        Olsen    colsen@gmail.com  011.44.1344.498718  30-03-1998       SA_REP    8000  0.20  145.0   80.0
62   162        Clara      Vishney  cvishney@gmail.com  011.44.1346.129268  11-11-1997       SA_REP   10500  0.25  147.0   80.0
42   142       Curtis       Davies   cdavies@gmail.com        650.121.2994  29-01-1997     ST_CLERK    3100   NaN  124.0   50.0
9    109       Daniel       Faviet   dfaviet@gmail.com        515.124.4169  16-08-1994   FI_ACCOUNT    9000   NaN  108.0  100.0
63   163     Danielle       Greene   dgreene@gmail.com  011.44.1346.229268  19-03-1999       SA_REP    9500  0.15  147.0   80.0
51   151        David    Bernstein  dbernste@gmail.com  011.44.1344.345268  24-03-1997       SA_REP    9500  0.25  145.0   80.0
5    105        David       Austin   daustin@gmail.com        590.423.4569  25-06-1997      IT_PROG    4800   NaN  103.0   60.0
65   165        David          Lee      dlee@gmail.com  011.44.1346.529268  23-02-2000       SA_REP    6800  0.10  147.0   80.0
14   114          Den     Raphaely  drapheal@gmail.com        515.127.4561  07-12-1994       PU_MAN   11000   NaN  100.0   30.0
7    107        Diana      Lorentz  dlorentz@gmail.com        590.423.5567  07-02-1999      IT_PROG    4200   NaN  103.0   60.0
98   198       Donald     OConnell  doconnel@gmail.com        650.507.9833  21-06-1999     SH_CLERK    2600   NaN  124.0   50.0
99   199      Douglas        Grant    dgrant@gmail.com        650.507.9844  13-01-2000     SH_CLERK    2600   NaN  124.0   50.0
49   149        Eleni      Zlotkey  ezlotkey@gmail.com  011.44.1344.429018  29-01-2000       SA_MAN   10500  0.20  100.0   80.0
72   172    Elizabeth        Bates    ebates@gmail.com  011.44.1343.529268  24-03-1999       SA_REP    7300  0.15  148.0   80.0
74   174        Ellen         Abel     eabel@gmail.com  011.44.1644.429267  11-05-1996       SA_REP   11000  0.30  149.0   80.0
48   148       Gerald    Cambrault  gcambrau@gmail.com  011.44.1344.619268  15-10-1999       SA_MAN   11000  0.30  100.0   80.0
83   183       Girard        Geoni    ggeoni@gmail.com        650.507.9879  03-02-2000     SH_CLERK    2800   NaN  120.0   50.0
18   118          Guy       Himuro   ghimuro@gmail.com        515.127.4565  15-11-1998     PU_CLERK    2600   NaN  114.0   30.0
69   169     Harrison        Bloom    hbloom@gmail.com  011.44.1343.829268  23-03-1998       SA_REP   10000  0.20  148.0   80.0
36   136        Hazel   Philtanker  hphiltan@gmail.com        650.127.1634  06-02-2000     ST_CLERK    2200   NaN  122.0   50.0
26   126        Irene  Mikkilineni  imikkili@gmail.com        650.124.1224  28-09-1998     ST_CLERK    2700   NaN  120.0   50.0
11   111       Ismael      Sciarra  isciarra@gmail.com        515.124.4369  30-09-1997   FI_ACCOUNT    7700   NaN  108.0  100.0
77   177         Jack   Livingston  jlivings@gmail.com  011.44.1644.429264  23-04-1998       SA_REP    8400  0.20  149.0   80.0
31   131        James       Marlow   jamrlow@gmail.com        650.124.7234  16-02-1997     ST_CLERK    2500   NaN  121.0   50.0
27   127        James       Landry   jlandry@gmail.com        650.124.1334  14-01-1999     ST_CLERK    2400   NaN  120.0   50.0
56   156      Janette         King     jking@gmail.com  011.44.1345.429268  30-01-1996       SA_REP   10000  0.35  146.0   80.0
33   133        Jason       Mallin   jmallin@gmail.com        650.127.1934  14-06-1996     ST_CLERK    3300   NaN  122.0   50.0
81   181         Jean       Fleaur   jfleaur@gmail.com        650.507.9877  23-02-1998     SH_CLERK    3100   NaN  120.0   50.0
100  200     Jennifer       Whalen   jwhalen@gmail.com        515.123.4444  17-09-1987      AD_ASST    4400   NaN  101.0   10.0
89   189     Jennifer        Dilly    jdilly@gmail.com        650.505.2876  13-08-1997     SH_CLERK    3600   NaN  122.0   50.0
39   139         John          Seo      jseo@gmail.com        650.121.2019  12-02-1998     ST_CLERK    2700   NaN  123.0   50.0
45   145         John      Russell   jrussel@gmail.com  011.44.1344.429268  01-10-1996       SA_MAN   14000  0.40  100.0   80.0
10   110         John         Chen     jchen@gmail.com        515.124.4269  28-09-1997   FI_ACCOUNT    8200   NaN  108.0  100.0
76   176     Jonathon       Taylor   jtaylor@gmail.com  011.44.1644.429265  24-03-1998       SA_REP    8600  0.20  149.0   80.0
12   112  Jose Manuel        Urman   jmurman@gmail.com        515.124.4469  07-03-1998   FI_ACCOUNT    7800   NaN  108.0  100.0
40   140       Joshua        Patel    jpatel@gmail.com        650.121.1834  06-04-1998     ST_CLERK    2500   NaN  123.0   20.0
25   125        Julia        Nayer    jnayer@gmail.com        650.124.1214  16-07-1997     ST_CLERK    3200   NaN  120.0   50.0
86   186        Julia    Dellinger  jdelling@gmail.com        650.509.3876  24-06-1998     SH_CLERK    3400   NaN  121.0   50.0
46   146        Karen     Partners  kpartner@gmail.com  011.44.1344.467268  05-01-1997       SA_MAN   13500  0.30  100.0   80.0
19   119        Karen   Colmenares  kcolmena@gmail.com        515.127.4566  10-08-1999     PU_CLERK    2500   NaN  114.0   30.0
88   188        Kelly        Chung    kchung@gmail.com        650.505.1876  14-06-1997     SH_CLERK    3800   NaN  122.0   50.0
97   197        Kevin       Feeney   kfeeney@gmail.com        650.507.9822  23-05-1998     SH_CLERK    3000   NaN  124.0   40.0
24   124        Kevin      Mourgos  kmourgos@gmail.com        650.123.5234  16-11-1999       ST_MAN    5800   NaN  100.0   50.0
35   135           Ki          Gee      kgee@gmail.com        650.127.1734  12-12-1999     ST_CLERK    2400   NaN  122.0   50.0
78   178    Kimberely        Grant    kgrant@gmail.com  011.44.1644.429263  24-05-1999       SA_REP    7000  0.15  149.0    NaN
29   129        Laura       Bissot   lbissot@gmail.com        650.124.5234  20-08-1997     ST_CLERK    3300   NaN  121.0   50.0
2    102          Lex      De Haan   ldehaan@gmail.com        515.123.4569  13-01-1993        AD_VP   17000   NaN  100.0   90.0
59   159      Lindsey        Smith    lsmith@gmail.com  011.44.1345.729268  10-03-1997       SA_REP    8000  0.30  146.0   80.0
68   168         Lisa         Ozer     lozer@gmail.com  011.44.1343.929268  11-03-1997       SA_REP   11500  0.25  148.0   80.0
60   160       Louise        Doran    ldoran@gmail.com  011.44.1345.629268  15-12-1997       SA_REP    7500  0.30  146.0   80.0
13   113         Luis         Popp     lpopp@gmail.com        515.124.4567  07-12-1999   FI_ACCOUNT    6900   NaN  108.0  100.0
82   182       Martha     Sullivan  msulliva@gmail.com        650.507.9878  21-06-1999     SH_CLERK    2500   NaN  120.0   50.0
64   164       Mattea      Marvins  mmarvins@gmail.com  011.44.1346.329268  24-01-2000       SA_REP    7200  0.10  147.0   80.0
20   120      Matthew        Weiss    mweiss@gmail.com        650.123.1234  18-07-1996       ST_MAN    8000   NaN  100.0   50.0
34   134      Michael       Rogers   mrogers@gmail.com        650.127.1834  26-08-1998     ST_CLERK    2900   NaN  122.0   50.0
30   130        Mozhe     Atkinson  matkinso@gmail.com        650.124.6234  30-10-1997     ST_CLERK    2800   NaN  121.0   50.0
8    108        Nancy    Greenberg  ngreenbe@gmail.com        515.124.4569  17-08-1994       FI_MGR   12000   NaN  101.0  100.0
84   184      Nandita     Sarchand  nsarchan@gmail.com        650.509.1876  27-01-1996     SH_CLERK    4200   NaN  121.0   50.0
54   154      Nanette    Cambrault  ncambrau@gmail.com  011.44.1344.987668  09-12-1998       SA_REP    7500  0.20  145.0   80.0
1    101        Neena      Kochhar  nkochhar@gmail.com        515.123.4568  21-09-1989        AD_VP   17000   NaN  100.0   90.0
55   155       Oliver      Tuvault  otuvault@gmail.com  011.44.1344.486508  23-11-1999       SA_REP    7000  0.15  145.0   80.0
57   157      Patrick        Sully    psully@gmail.com  011.44.1345.929268  04-03-1996       SA_REP    9500  0.35  146.0   80.0
22   122        Payam     Kaufling  pkauflin@gmail.com        650.123.3234  01-05-1995       ST_MAN    7900   NaN  100.0   50.0
50   150        Peter       Tucker   ptucker@gmail.com  011.44.1344.129268  30-01-1997       SA_REP   10000  0.30  145.0   80.0
52   152        Peter         Hall     phall@gmail.com  011.44.1344.478968  20-08-1997       SA_REP    9000  0.25  145.0   80.0
44   144        Peter       Vargas   pvargas@gmail.com        650.121.2004  09-07-1998     ST_CLERK    2500   NaN  124.0   50.0
43   143      Randall        Matos    rmatos@gmail.com        650.121.2874  15-03-1998     ST_CLERK    2600   NaN  124.0   50.0
91   191      Randall      Perkins  rperkins@gmail.com        650.505.4876  19-12-1999     SH_CLERK    2500   NaN  122.0   50.0
37   137       Renske       Ladwig   rladwig@gmail.com        650.121.1234  14-07-1995     ST_CLERK    3600   NaN  123.0   50.0
94   194       Samuel       McCain   smccain@gmail.com        650.501.3876  01-07-1998     SH_CLERK    3200   NaN  123.0   40.0
92   192        Sarah         Bell     sbell@gmail.com        650.501.1876  04-02-1996     SH_CLERK    4000   NaN  123.0   50.0
61   161       Sarath       Sewall   ssewall@gmail.com  011.44.1345.529268  03-11-1998       SA_REP    7000  0.25  146.0   80.0
23   123       Shanta      Vollman  svollman@gmail.com        650.123.4234  10-10-1997       ST_MAN    6500   NaN  100.0   50.0
16   116       Shelli        Baida    sbaida@gmail.com        515.127.4563  24-12-1997     PU_CLERK    2900   NaN  114.0   30.0
17   117        Sigal       Tobias   stobias@gmail.com        515.127.4564  24-07-1997     PU_CLERK    2800   NaN  114.0   30.0
38   138      Stephen       Stiles   sstiles@gmail.com        650.121.2034  26-10-1997     ST_CLERK    3200   NaN  123.0   50.0
0    100       Steven         King     sking@gmail.com        515.123.4567  17-06-1987      AD_PRES   24000   NaN    NaN   90.0
28   128       Steven       Markle   smarkle@gmail.com        650.124.1434  08-03-2000     ST_CLERK    2200   NaN  120.0   50.0
66   166       Sundar         Ande     sande@gmail.com  011.44.1346.629268  24-03-2000       SA_REP    6400  0.10  147.0   80.0
73   173      Sundita        Kumar    skumar@gmail.com  011.44.1343.329268  21-04-2000       SA_REP    6100  0.10  148.0   80.0
32   132           TJ        Olson   tjolson@gmail.com        650.124.8234  10-04-1999     ST_CLERK    2100   NaN  121.0   50.0
70   170       Tayler          Fox      tfox@gmail.com  011.44.1343.729268  24-01-1998       SA_REP    9600  0.20  148.0   80.0
90   190      Timothy        Gates    tgates@gmail.com        650.505.3876  11-07-1998     SH_CLERK    2900   NaN  122.0   50.0
41   141       Trenna         Rajs     trajs@gmail.com        650.121.8009  17-10-1995     ST_CLERK    3500   NaN  124.0   20.0
6    106        Valli    Pataballa  vpatabal@gmail.com        590.423.4560  05-02-1998      IT_PROG    4800   NaN  103.0   60.0
95   195        Vance        Jones    vjones@gmail.com        650.501.4876  17-03-1999     SH_CLERK    2800   NaN  123.0   40.0
71   171      William        Smith    wsmith@gmail.com  011.44.1343.629268  23-02-1999       SA_REP    7400  0.15  148.0   80.0
80   180      Winston       Taylor   wtaylor@gmail.com        650.507.9876  24-01-1998     SH_CLERK    3200   NaN  120.0   50.0
>>> res.sort_values(by='fname',ascending=False)
     eid        fname        lname               email               phone     hiredate       jobid  salary  comm    mid    did
80   180      Winston       Taylor   wtaylor@gmail.com        650.507.9876  24-01-1998     SH_CLERK    3200   NaN  120.0   50.0
71   171      William        Smith    wsmith@gmail.com  011.44.1343.629268  23-02-1999       SA_REP    7400  0.15  148.0   80.0
95   195        Vance        Jones    vjones@gmail.com        650.501.4876  17-03-1999     SH_CLERK    2800   NaN  123.0   40.0
6    106        Valli    Pataballa  vpatabal@gmail.com        590.423.4560  05-02-1998      IT_PROG    4800   NaN  103.0   60.0
41   141       Trenna         Rajs     trajs@gmail.com        650.121.8009  17-10-1995     ST_CLERK    3500   NaN  124.0   20.0
90   190      Timothy        Gates    tgates@gmail.com        650.505.3876  11-07-1998     SH_CLERK    2900   NaN  122.0   50.0
70   170       Tayler          Fox      tfox@gmail.com  011.44.1343.729268  24-01-1998       SA_REP    9600  0.20  148.0   80.0
32   132           TJ        Olson   tjolson@gmail.com        650.124.8234  10-04-1999     ST_CLERK    2100   NaN  121.0   50.0
73   173      Sundita        Kumar    skumar@gmail.com  011.44.1343.329268  21-04-2000       SA_REP    6100  0.10  148.0   80.0
66   166       Sundar         Ande     sande@gmail.com  011.44.1346.629268  24-03-2000       SA_REP    6400  0.10  147.0   80.0
28   128       Steven       Markle   smarkle@gmail.com        650.124.1434  08-03-2000     ST_CLERK    2200   NaN  120.0   50.0
0    100       Steven         King     sking@gmail.com        515.123.4567  17-06-1987      AD_PRES   24000   NaN    NaN   90.0
38   138      Stephen       Stiles   sstiles@gmail.com        650.121.2034  26-10-1997     ST_CLERK    3200   NaN  123.0   50.0
17   117        Sigal       Tobias   stobias@gmail.com        515.127.4564  24-07-1997     PU_CLERK    2800   NaN  114.0   30.0
16   116       Shelli        Baida    sbaida@gmail.com        515.127.4563  24-12-1997     PU_CLERK    2900   NaN  114.0   30.0
23   123       Shanta      Vollman  svollman@gmail.com        650.123.4234  10-10-1997       ST_MAN    6500   NaN  100.0   50.0
61   161       Sarath       Sewall   ssewall@gmail.com  011.44.1345.529268  03-11-1998       SA_REP    7000  0.25  146.0   80.0
92   192        Sarah         Bell     sbell@gmail.com        650.501.1876  04-02-1996     SH_CLERK    4000   NaN  123.0   50.0
94   194       Samuel       McCain   smccain@gmail.com        650.501.3876  01-07-1998     SH_CLERK    3200   NaN  123.0   40.0
37   137       Renske       Ladwig   rladwig@gmail.com        650.121.1234  14-07-1995     ST_CLERK    3600   NaN  123.0   50.0
91   191      Randall      Perkins  rperkins@gmail.com        650.505.4876  19-12-1999     SH_CLERK    2500   NaN  122.0   50.0
43   143      Randall        Matos    rmatos@gmail.com        650.121.2874  15-03-1998     ST_CLERK    2600   NaN  124.0   50.0
52   152        Peter         Hall     phall@gmail.com  011.44.1344.478968  20-08-1997       SA_REP    9000  0.25  145.0   80.0
44   144        Peter       Vargas   pvargas@gmail.com        650.121.2004  09-07-1998     ST_CLERK    2500   NaN  124.0   50.0
50   150        Peter       Tucker   ptucker@gmail.com  011.44.1344.129268  30-01-1997       SA_REP   10000  0.30  145.0   80.0
22   122        Payam     Kaufling  pkauflin@gmail.com        650.123.3234  01-05-1995       ST_MAN    7900   NaN  100.0   50.0
57   157      Patrick        Sully    psully@gmail.com  011.44.1345.929268  04-03-1996       SA_REP    9500  0.35  146.0   80.0
55   155       Oliver      Tuvault  otuvault@gmail.com  011.44.1344.486508  23-11-1999       SA_REP    7000  0.15  145.0   80.0
1    101        Neena      Kochhar  nkochhar@gmail.com        515.123.4568  21-09-1989        AD_VP   17000   NaN  100.0   90.0
54   154      Nanette    Cambrault  ncambrau@gmail.com  011.44.1344.987668  09-12-1998       SA_REP    7500  0.20  145.0   80.0
84   184      Nandita     Sarchand  nsarchan@gmail.com        650.509.1876  27-01-1996     SH_CLERK    4200   NaN  121.0   50.0
8    108        Nancy    Greenberg  ngreenbe@gmail.com        515.124.4569  17-08-1994       FI_MGR   12000   NaN  101.0  100.0
30   130        Mozhe     Atkinson  matkinso@gmail.com        650.124.6234  30-10-1997     ST_CLERK    2800   NaN  121.0   50.0
34   134      Michael       Rogers   mrogers@gmail.com        650.127.1834  26-08-1998     ST_CLERK    2900   NaN  122.0   50.0
20   120      Matthew        Weiss    mweiss@gmail.com        650.123.1234  18-07-1996       ST_MAN    8000   NaN  100.0   50.0
64   164       Mattea      Marvins  mmarvins@gmail.com  011.44.1346.329268  24-01-2000       SA_REP    7200  0.10  147.0   80.0
82   182       Martha     Sullivan  msulliva@gmail.com        650.507.9878  21-06-1999     SH_CLERK    2500   NaN  120.0   50.0
13   113         Luis         Popp     lpopp@gmail.com        515.124.4567  07-12-1999   FI_ACCOUNT    6900   NaN  108.0  100.0
60   160       Louise        Doran    ldoran@gmail.com  011.44.1345.629268  15-12-1997       SA_REP    7500  0.30  146.0   80.0
68   168         Lisa         Ozer     lozer@gmail.com  011.44.1343.929268  11-03-1997       SA_REP   11500  0.25  148.0   80.0
59   159      Lindsey        Smith    lsmith@gmail.com  011.44.1345.729268  10-03-1997       SA_REP    8000  0.30  146.0   80.0
2    102          Lex      De Haan   ldehaan@gmail.com        515.123.4569  13-01-1993        AD_VP   17000   NaN  100.0   90.0
29   129        Laura       Bissot   lbissot@gmail.com        650.124.5234  20-08-1997     ST_CLERK    3300   NaN  121.0   50.0
78   178    Kimberely        Grant    kgrant@gmail.com  011.44.1644.429263  24-05-1999       SA_REP    7000  0.15  149.0    NaN
35   135           Ki          Gee      kgee@gmail.com        650.127.1734  12-12-1999     ST_CLERK    2400   NaN  122.0   50.0
97   197        Kevin       Feeney   kfeeney@gmail.com        650.507.9822  23-05-1998     SH_CLERK    3000   NaN  124.0   40.0
24   124        Kevin      Mourgos  kmourgos@gmail.com        650.123.5234  16-11-1999       ST_MAN    5800   NaN  100.0   50.0
88   188        Kelly        Chung    kchung@gmail.com        650.505.1876  14-06-1997     SH_CLERK    3800   NaN  122.0   50.0
19   119        Karen   Colmenares  kcolmena@gmail.com        515.127.4566  10-08-1999     PU_CLERK    2500   NaN  114.0   30.0
46   146        Karen     Partners  kpartner@gmail.com  011.44.1344.467268  05-01-1997       SA_MAN   13500  0.30  100.0   80.0
25   125        Julia        Nayer    jnayer@gmail.com        650.124.1214  16-07-1997     ST_CLERK    3200   NaN  120.0   50.0
86   186        Julia    Dellinger  jdelling@gmail.com        650.509.3876  24-06-1998     SH_CLERK    3400   NaN  121.0   50.0
40   140       Joshua        Patel    jpatel@gmail.com        650.121.1834  06-04-1998     ST_CLERK    2500   NaN  123.0   20.0
12   112  Jose Manuel        Urman   jmurman@gmail.com        515.124.4469  07-03-1998   FI_ACCOUNT    7800   NaN  108.0  100.0
76   176     Jonathon       Taylor   jtaylor@gmail.com  011.44.1644.429265  24-03-1998       SA_REP    8600  0.20  149.0   80.0
39   139         John          Seo      jseo@gmail.com        650.121.2019  12-02-1998     ST_CLERK    2700   NaN  123.0   50.0
45   145         John      Russell   jrussel@gmail.com  011.44.1344.429268  01-10-1996       SA_MAN   14000  0.40  100.0   80.0
10   110         John         Chen     jchen@gmail.com        515.124.4269  28-09-1997   FI_ACCOUNT    8200   NaN  108.0  100.0
89   189     Jennifer        Dilly    jdilly@gmail.com        650.505.2876  13-08-1997     SH_CLERK    3600   NaN  122.0   50.0
100  200     Jennifer       Whalen   jwhalen@gmail.com        515.123.4444  17-09-1987      AD_ASST    4400   NaN  101.0   10.0
81   181         Jean       Fleaur   jfleaur@gmail.com        650.507.9877  23-02-1998     SH_CLERK    3100   NaN  120.0   50.0
33   133        Jason       Mallin   jmallin@gmail.com        650.127.1934  14-06-1996     ST_CLERK    3300   NaN  122.0   50.0
56   156      Janette         King     jking@gmail.com  011.44.1345.429268  30-01-1996       SA_REP   10000  0.35  146.0   80.0
31   131        James       Marlow   jamrlow@gmail.com        650.124.7234  16-02-1997     ST_CLERK    2500   NaN  121.0   50.0
27   127        James       Landry   jlandry@gmail.com        650.124.1334  14-01-1999     ST_CLERK    2400   NaN  120.0   50.0
77   177         Jack   Livingston  jlivings@gmail.com  011.44.1644.429264  23-04-1998       SA_REP    8400  0.20  149.0   80.0
11   111       Ismael      Sciarra  isciarra@gmail.com        515.124.4369  30-09-1997   FI_ACCOUNT    7700   NaN  108.0  100.0
26   126        Irene  Mikkilineni  imikkili@gmail.com        650.124.1224  28-09-1998     ST_CLERK    2700   NaN  120.0   50.0
36   136        Hazel   Philtanker  hphiltan@gmail.com        650.127.1634  06-02-2000     ST_CLERK    2200   NaN  122.0   50.0
69   169     Harrison        Bloom    hbloom@gmail.com  011.44.1343.829268  23-03-1998       SA_REP   10000  0.20  148.0   80.0
18   118          Guy       Himuro   ghimuro@gmail.com        515.127.4565  15-11-1998     PU_CLERK    2600   NaN  114.0   30.0
83   183       Girard        Geoni    ggeoni@gmail.com        650.507.9879  03-02-2000     SH_CLERK    2800   NaN  120.0   50.0
48   148       Gerald    Cambrault  gcambrau@gmail.com  011.44.1344.619268  15-10-1999       SA_MAN   11000  0.30  100.0   80.0
74   174        Ellen         Abel     eabel@gmail.com  011.44.1644.429267  11-05-1996       SA_REP   11000  0.30  149.0   80.0
72   172    Elizabeth        Bates    ebates@gmail.com  011.44.1343.529268  24-03-1999       SA_REP    7300  0.15  148.0   80.0
49   149        Eleni      Zlotkey  ezlotkey@gmail.com  011.44.1344.429018  29-01-2000       SA_MAN   10500  0.20  100.0   80.0
99   199      Douglas        Grant    dgrant@gmail.com        650.507.9844  13-01-2000     SH_CLERK    2600   NaN  124.0   50.0
98   198       Donald     OConnell  doconnel@gmail.com        650.507.9833  21-06-1999     SH_CLERK    2600   NaN  124.0   50.0
7    107        Diana      Lorentz  dlorentz@gmail.com        590.423.5567  07-02-1999      IT_PROG    4200   NaN  103.0   60.0
14   114          Den     Raphaely  drapheal@gmail.com        515.127.4561  07-12-1994       PU_MAN   11000   NaN  100.0   30.0
51   151        David    Bernstein  dbernste@gmail.com  011.44.1344.345268  24-03-1997       SA_REP    9500  0.25  145.0   80.0
65   165        David          Lee      dlee@gmail.com  011.44.1346.529268  23-02-2000       SA_REP    6800  0.10  147.0   80.0
5    105        David       Austin   daustin@gmail.com        590.423.4569  25-06-1997      IT_PROG    4800   NaN  103.0   60.0
63   163     Danielle       Greene   dgreene@gmail.com  011.44.1346.229268  19-03-1999       SA_REP    9500  0.15  147.0   80.0
9    109       Daniel       Faviet   dfaviet@gmail.com        515.124.4169  16-08-1994   FI_ACCOUNT    9000   NaN  108.0  100.0
42   142       Curtis       Davies   cdavies@gmail.com        650.121.2994  29-01-1997     ST_CLERK    3100   NaN  124.0   50.0
62   162        Clara      Vishney  cvishney@gmail.com  011.44.1346.129268  11-11-1997       SA_REP   10500  0.25  147.0   80.0
53   153  Christopher        Olsen    colsen@gmail.com  011.44.1344.498718  30-03-1998       SA_REP    8000  0.20  145.0   80.0
79   179      Charles      Johnson  cjohnson@gmail.com  011.44.1644.429262  04-01-2000       SA_REP    6200  0.10  149.0   80.0
4    104        Bruce        Ernst    bernst@gmail.com        590.423.4568  21-05-1991      IT_PROG    6000   NaN  103.0   60.0
93   193      Britney      Everett  beverett@gmail.com        650.501.2876  03-03-1997     SH_CLERK    3900   NaN  123.0   50.0
87   187      Anthony       Cabrio   acabrio@gmail.com        650.509.4876  07-02-1999     SH_CLERK    3000   NaN  121.0   50.0
67   167         Amit        Banda    abanda@gmail.com  011.44.1346.729268  21-04-2000       SA_REP    6200  0.10  147.0   80.0
75   175       Alyssa       Hutton   ahutton@gmail.com  011.44.1644.429266  19-03-1997       SA_REP    8800  0.25  149.0   80.0
58   158        Allan       McEwen   amcewen@gmail.com  011.44.1345.829268  01-08-1996       SA_REP    9000  0.35  146.0   80.0
85   185       Alexis         Bull     abull@gmail.com        650.509.2876  20-02-1997     SH_CLERK    4100   NaN  121.0   50.0
3    103    Alexander       Hunold   ahunold@gmail.com        590.423.4567  03-01-1990      IT_PROG    9000   NaN  102.0   60.0
15   115    Alexander         Khoo   akhoo@gmail.co.in        515.127.4562  18-05-1995     PU_CLERK    3100   NaN  114.0   30.0
47   147      Alberto    Errazuriz  aerrazur@gmail.com  011.44.1344.429278  10-03-1997       SA_MAN   12000  0.30  100.0   80.0
96   196        Alana        Walsh    awalsh@gmail.com        650.507.9811  24-04-1998     SH_CLERK    3100   NaN  124.0   40.0
21   121         Adam        Fripp    afripp@gmail.com        650.123.2234  10-04-1997       ST_MAN    8200   NaN  100.0   50.0
>>> 
>>> res.sort_values(by=['did','salary'],ascending=[True,False])
     eid        fname        lname               email               phone     hiredate       jobid  salary  comm    mid    did
100  200     Jennifer       Whalen   jwhalen@gmail.com        515.123.4444  17-09-1987      AD_ASST    4400   NaN  101.0   10.0
41   141       Trenna         Rajs     trajs@gmail.com        650.121.8009  17-10-1995     ST_CLERK    3500   NaN  124.0   20.0
40   140       Joshua        Patel    jpatel@gmail.com        650.121.1834  06-04-1998     ST_CLERK    2500   NaN  123.0   20.0
14   114          Den     Raphaely  drapheal@gmail.com        515.127.4561  07-12-1994       PU_MAN   11000   NaN  100.0   30.0
15   115    Alexander         Khoo   akhoo@gmail.co.in        515.127.4562  18-05-1995     PU_CLERK    3100   NaN  114.0   30.0
16   116       Shelli        Baida    sbaida@gmail.com        515.127.4563  24-12-1997     PU_CLERK    2900   NaN  114.0   30.0
17   117        Sigal       Tobias   stobias@gmail.com        515.127.4564  24-07-1997     PU_CLERK    2800   NaN  114.0   30.0
18   118          Guy       Himuro   ghimuro@gmail.com        515.127.4565  15-11-1998     PU_CLERK    2600   NaN  114.0   30.0
19   119        Karen   Colmenares  kcolmena@gmail.com        515.127.4566  10-08-1999     PU_CLERK    2500   NaN  114.0   30.0
94   194       Samuel       McCain   smccain@gmail.com        650.501.3876  01-07-1998     SH_CLERK    3200   NaN  123.0   40.0
96   196        Alana        Walsh    awalsh@gmail.com        650.507.9811  24-04-1998     SH_CLERK    3100   NaN  124.0   40.0
97   197        Kevin       Feeney   kfeeney@gmail.com        650.507.9822  23-05-1998     SH_CLERK    3000   NaN  124.0   40.0
95   195        Vance        Jones    vjones@gmail.com        650.501.4876  17-03-1999     SH_CLERK    2800   NaN  123.0   40.0
21   121         Adam        Fripp    afripp@gmail.com        650.123.2234  10-04-1997       ST_MAN    8200   NaN  100.0   50.0
20   120      Matthew        Weiss    mweiss@gmail.com        650.123.1234  18-07-1996       ST_MAN    8000   NaN  100.0   50.0
22   122        Payam     Kaufling  pkauflin@gmail.com        650.123.3234  01-05-1995       ST_MAN    7900   NaN  100.0   50.0
23   123       Shanta      Vollman  svollman@gmail.com        650.123.4234  10-10-1997       ST_MAN    6500   NaN  100.0   50.0
24   124        Kevin      Mourgos  kmourgos@gmail.com        650.123.5234  16-11-1999       ST_MAN    5800   NaN  100.0   50.0
84   184      Nandita     Sarchand  nsarchan@gmail.com        650.509.1876  27-01-1996     SH_CLERK    4200   NaN  121.0   50.0
85   185       Alexis         Bull     abull@gmail.com        650.509.2876  20-02-1997     SH_CLERK    4100   NaN  121.0   50.0
92   192        Sarah         Bell     sbell@gmail.com        650.501.1876  04-02-1996     SH_CLERK    4000   NaN  123.0   50.0
93   193      Britney      Everett  beverett@gmail.com        650.501.2876  03-03-1997     SH_CLERK    3900   NaN  123.0   50.0
88   188        Kelly        Chung    kchung@gmail.com        650.505.1876  14-06-1997     SH_CLERK    3800   NaN  122.0   50.0
37   137       Renske       Ladwig   rladwig@gmail.com        650.121.1234  14-07-1995     ST_CLERK    3600   NaN  123.0   50.0
89   189     Jennifer        Dilly    jdilly@gmail.com        650.505.2876  13-08-1997     SH_CLERK    3600   NaN  122.0   50.0
86   186        Julia    Dellinger  jdelling@gmail.com        650.509.3876  24-06-1998     SH_CLERK    3400   NaN  121.0   50.0
29   129        Laura       Bissot   lbissot@gmail.com        650.124.5234  20-08-1997     ST_CLERK    3300   NaN  121.0   50.0
33   133        Jason       Mallin   jmallin@gmail.com        650.127.1934  14-06-1996     ST_CLERK    3300   NaN  122.0   50.0
25   125        Julia        Nayer    jnayer@gmail.com        650.124.1214  16-07-1997     ST_CLERK    3200   NaN  120.0   50.0
38   138      Stephen       Stiles   sstiles@gmail.com        650.121.2034  26-10-1997     ST_CLERK    3200   NaN  123.0   50.0
80   180      Winston       Taylor   wtaylor@gmail.com        650.507.9876  24-01-1998     SH_CLERK    3200   NaN  120.0   50.0
42   142       Curtis       Davies   cdavies@gmail.com        650.121.2994  29-01-1997     ST_CLERK    3100   NaN  124.0   50.0
81   181         Jean       Fleaur   jfleaur@gmail.com        650.507.9877  23-02-1998     SH_CLERK    3100   NaN  120.0   50.0
87   187      Anthony       Cabrio   acabrio@gmail.com        650.509.4876  07-02-1999     SH_CLERK    3000   NaN  121.0   50.0
34   134      Michael       Rogers   mrogers@gmail.com        650.127.1834  26-08-1998     ST_CLERK    2900   NaN  122.0   50.0
90   190      Timothy        Gates    tgates@gmail.com        650.505.3876  11-07-1998     SH_CLERK    2900   NaN  122.0   50.0
30   130        Mozhe     Atkinson  matkinso@gmail.com        650.124.6234  30-10-1997     ST_CLERK    2800   NaN  121.0   50.0
83   183       Girard        Geoni    ggeoni@gmail.com        650.507.9879  03-02-2000     SH_CLERK    2800   NaN  120.0   50.0
26   126        Irene  Mikkilineni  imikkili@gmail.com        650.124.1224  28-09-1998     ST_CLERK    2700   NaN  120.0   50.0
39   139         John          Seo      jseo@gmail.com        650.121.2019  12-02-1998     ST_CLERK    2700   NaN  123.0   50.0
43   143      Randall        Matos    rmatos@gmail.com        650.121.2874  15-03-1998     ST_CLERK    2600   NaN  124.0   50.0
98   198       Donald     OConnell  doconnel@gmail.com        650.507.9833  21-06-1999     SH_CLERK    2600   NaN  124.0   50.0
99   199      Douglas        Grant    dgrant@gmail.com        650.507.9844  13-01-2000     SH_CLERK    2600   NaN  124.0   50.0
31   131        James       Marlow   jamrlow@gmail.com        650.124.7234  16-02-1997     ST_CLERK    2500   NaN  121.0   50.0
44   144        Peter       Vargas   pvargas@gmail.com        650.121.2004  09-07-1998     ST_CLERK    2500   NaN  124.0   50.0
82   182       Martha     Sullivan  msulliva@gmail.com        650.507.9878  21-06-1999     SH_CLERK    2500   NaN  120.0   50.0
91   191      Randall      Perkins  rperkins@gmail.com        650.505.4876  19-12-1999     SH_CLERK    2500   NaN  122.0   50.0
27   127        James       Landry   jlandry@gmail.com        650.124.1334  14-01-1999     ST_CLERK    2400   NaN  120.0   50.0
35   135           Ki          Gee      kgee@gmail.com        650.127.1734  12-12-1999     ST_CLERK    2400   NaN  122.0   50.0
28   128       Steven       Markle   smarkle@gmail.com        650.124.1434  08-03-2000     ST_CLERK    2200   NaN  120.0   50.0
36   136        Hazel   Philtanker  hphiltan@gmail.com        650.127.1634  06-02-2000     ST_CLERK    2200   NaN  122.0   50.0
32   132           TJ        Olson   tjolson@gmail.com        650.124.8234  10-04-1999     ST_CLERK    2100   NaN  121.0   50.0
3    103    Alexander       Hunold   ahunold@gmail.com        590.423.4567  03-01-1990      IT_PROG    9000   NaN  102.0   60.0
4    104        Bruce        Ernst    bernst@gmail.com        590.423.4568  21-05-1991      IT_PROG    6000   NaN  103.0   60.0
5    105        David       Austin   daustin@gmail.com        590.423.4569  25-06-1997      IT_PROG    4800   NaN  103.0   60.0
6    106        Valli    Pataballa  vpatabal@gmail.com        590.423.4560  05-02-1998      IT_PROG    4800   NaN  103.0   60.0
7    107        Diana      Lorentz  dlorentz@gmail.com        590.423.5567  07-02-1999      IT_PROG    4200   NaN  103.0   60.0
45   145         John      Russell   jrussel@gmail.com  011.44.1344.429268  01-10-1996       SA_MAN   14000  0.40  100.0   80.0
46   146        Karen     Partners  kpartner@gmail.com  011.44.1344.467268  05-01-1997       SA_MAN   13500  0.30  100.0   80.0
47   147      Alberto    Errazuriz  aerrazur@gmail.com  011.44.1344.429278  10-03-1997       SA_MAN   12000  0.30  100.0   80.0
68   168         Lisa         Ozer     lozer@gmail.com  011.44.1343.929268  11-03-1997       SA_REP   11500  0.25  148.0   80.0
48   148       Gerald    Cambrault  gcambrau@gmail.com  011.44.1344.619268  15-10-1999       SA_MAN   11000  0.30  100.0   80.0
74   174        Ellen         Abel     eabel@gmail.com  011.44.1644.429267  11-05-1996       SA_REP   11000  0.30  149.0   80.0
49   149        Eleni      Zlotkey  ezlotkey@gmail.com  011.44.1344.429018  29-01-2000       SA_MAN   10500  0.20  100.0   80.0
62   162        Clara      Vishney  cvishney@gmail.com  011.44.1346.129268  11-11-1997       SA_REP   10500  0.25  147.0   80.0
50   150        Peter       Tucker   ptucker@gmail.com  011.44.1344.129268  30-01-1997       SA_REP   10000  0.30  145.0   80.0
56   156      Janette         King     jking@gmail.com  011.44.1345.429268  30-01-1996       SA_REP   10000  0.35  146.0   80.0
69   169     Harrison        Bloom    hbloom@gmail.com  011.44.1343.829268  23-03-1998       SA_REP   10000  0.20  148.0   80.0
70   170       Tayler          Fox      tfox@gmail.com  011.44.1343.729268  24-01-1998       SA_REP    9600  0.20  148.0   80.0
51   151        David    Bernstein  dbernste@gmail.com  011.44.1344.345268  24-03-1997       SA_REP    9500  0.25  145.0   80.0
57   157      Patrick        Sully    psully@gmail.com  011.44.1345.929268  04-03-1996       SA_REP    9500  0.35  146.0   80.0
63   163     Danielle       Greene   dgreene@gmail.com  011.44.1346.229268  19-03-1999       SA_REP    9500  0.15  147.0   80.0
52   152        Peter         Hall     phall@gmail.com  011.44.1344.478968  20-08-1997       SA_REP    9000  0.25  145.0   80.0
58   158        Allan       McEwen   amcewen@gmail.com  011.44.1345.829268  01-08-1996       SA_REP    9000  0.35  146.0   80.0
75   175       Alyssa       Hutton   ahutton@gmail.com  011.44.1644.429266  19-03-1997       SA_REP    8800  0.25  149.0   80.0
76   176     Jonathon       Taylor   jtaylor@gmail.com  011.44.1644.429265  24-03-1998       SA_REP    8600  0.20  149.0   80.0
77   177         Jack   Livingston  jlivings@gmail.com  011.44.1644.429264  23-04-1998       SA_REP    8400  0.20  149.0   80.0
53   153  Christopher        Olsen    colsen@gmail.com  011.44.1344.498718  30-03-1998       SA_REP    8000  0.20  145.0   80.0
59   159      Lindsey        Smith    lsmith@gmail.com  011.44.1345.729268  10-03-1997       SA_REP    8000  0.30  146.0   80.0
54   154      Nanette    Cambrault  ncambrau@gmail.com  011.44.1344.987668  09-12-1998       SA_REP    7500  0.20  145.0   80.0
60   160       Louise        Doran    ldoran@gmail.com  011.44.1345.629268  15-12-1997       SA_REP    7500  0.30  146.0   80.0
71   171      William        Smith    wsmith@gmail.com  011.44.1343.629268  23-02-1999       SA_REP    7400  0.15  148.0   80.0
72   172    Elizabeth        Bates    ebates@gmail.com  011.44.1343.529268  24-03-1999       SA_REP    7300  0.15  148.0   80.0
64   164       Mattea      Marvins  mmarvins@gmail.com  011.44.1346.329268  24-01-2000       SA_REP    7200  0.10  147.0   80.0
55   155       Oliver      Tuvault  otuvault@gmail.com  011.44.1344.486508  23-11-1999       SA_REP    7000  0.15  145.0   80.0
61   161       Sarath       Sewall   ssewall@gmail.com  011.44.1345.529268  03-11-1998       SA_REP    7000  0.25  146.0   80.0
65   165        David          Lee      dlee@gmail.com  011.44.1346.529268  23-02-2000       SA_REP    6800  0.10  147.0   80.0
66   166       Sundar         Ande     sande@gmail.com  011.44.1346.629268  24-03-2000       SA_REP    6400  0.10  147.0   80.0
67   167         Amit        Banda    abanda@gmail.com  011.44.1346.729268  21-04-2000       SA_REP    6200  0.10  147.0   80.0
79   179      Charles      Johnson  cjohnson@gmail.com  011.44.1644.429262  04-01-2000       SA_REP    6200  0.10  149.0   80.0
73   173      Sundita        Kumar    skumar@gmail.com  011.44.1343.329268  21-04-2000       SA_REP    6100  0.10  148.0   80.0
0    100       Steven         King     sking@gmail.com        515.123.4567  17-06-1987      AD_PRES   24000   NaN    NaN   90.0
1    101        Neena      Kochhar  nkochhar@gmail.com        515.123.4568  21-09-1989        AD_VP   17000   NaN  100.0   90.0
2    102          Lex      De Haan   ldehaan@gmail.com        515.123.4569  13-01-1993        AD_VP   17000   NaN  100.0   90.0
8    108        Nancy    Greenberg  ngreenbe@gmail.com        515.124.4569  17-08-1994       FI_MGR   12000   NaN  101.0  100.0
9    109       Daniel       Faviet   dfaviet@gmail.com        515.124.4169  16-08-1994   FI_ACCOUNT    9000   NaN  108.0  100.0
10   110         John         Chen     jchen@gmail.com        515.124.4269  28-09-1997   FI_ACCOUNT    8200   NaN  108.0  100.0
12   112  Jose Manuel        Urman   jmurman@gmail.com        515.124.4469  07-03-1998   FI_ACCOUNT    7800   NaN  108.0  100.0
11   111       Ismael      Sciarra  isciarra@gmail.com        515.124.4369  30-09-1997   FI_ACCOUNT    7700   NaN  108.0  100.0
13   113         Luis         Popp     lpopp@gmail.com        515.124.4567  07-12-1999   FI_ACCOUNT    6900   NaN  108.0  100.0
78   178    Kimberely        Grant    kgrant@gmail.com  011.44.1644.429263  24-05-1999       SA_REP    7000  0.15  149.0    NaN
>>> res.sort_values(by=['did','salary'],ascending=[True,False])['did','salary']
Traceback (most recent call last):
  File "C:\Python37\lib\site-packages\pandas\core\indexes\base.py", line 2897, in get_loc
    return self._engine.get_loc(key)
  File "pandas/_libs/index.pyx", line 107, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 131, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 1607, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 1614, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: ('did', 'salary')

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    res.sort_values(by=['did','salary'],ascending=[True,False])['did','salary']
  File "C:\Python37\lib\site-packages\pandas\core\frame.py", line 2995, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Python37\lib\site-packages\pandas\core\indexes\base.py", line 2899, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas/_libs/index.pyx", line 107, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 131, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 1607, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 1614, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: ('did', 'salary')
>>> (res.sort_values(by=['did','salary'],ascending=[True,False]))['did','salary']
Traceback (most recent call last):
  File "C:\Python37\lib\site-packages\pandas\core\indexes\base.py", line 2897, in get_loc
    return self._engine.get_loc(key)
  File "pandas/_libs/index.pyx", line 107, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 131, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 1607, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 1614, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: ('did', 'salary')

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    (res.sort_values(by=['did','salary'],ascending=[True,False]))['did','salary']
  File "C:\Python37\lib\site-packages\pandas\core\frame.py", line 2995, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Python37\lib\site-packages\pandas\core\indexes\base.py", line 2899, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas/_libs/index.pyx", line 107, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 131, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 1607, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 1614, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: ('did', 'salary')
>>> (res.sort_values(by=['did','salary'],ascending=[True,False]))
     eid        fname        lname               email               phone     hiredate       jobid  salary  comm    mid    did
100  200     Jennifer       Whalen   jwhalen@gmail.com        515.123.4444  17-09-1987      AD_ASST    4400   NaN  101.0   10.0
41   141       Trenna         Rajs     trajs@gmail.com        650.121.8009  17-10-1995     ST_CLERK    3500   NaN  124.0   20.0
40   140       Joshua        Patel    jpatel@gmail.com        650.121.1834  06-04-1998     ST_CLERK    2500   NaN  123.0   20.0
14   114          Den     Raphaely  drapheal@gmail.com        515.127.4561  07-12-1994       PU_MAN   11000   NaN  100.0   30.0
15   115    Alexander         Khoo   akhoo@gmail.co.in        515.127.4562  18-05-1995     PU_CLERK    3100   NaN  114.0   30.0
16   116       Shelli        Baida    sbaida@gmail.com        515.127.4563  24-12-1997     PU_CLERK    2900   NaN  114.0   30.0
17   117        Sigal       Tobias   stobias@gmail.com        515.127.4564  24-07-1997     PU_CLERK    2800   NaN  114.0   30.0
18   118          Guy       Himuro   ghimuro@gmail.com        515.127.4565  15-11-1998     PU_CLERK    2600   NaN  114.0   30.0
19   119        Karen   Colmenares  kcolmena@gmail.com        515.127.4566  10-08-1999     PU_CLERK    2500   NaN  114.0   30.0
94   194       Samuel       McCain   smccain@gmail.com        650.501.3876  01-07-1998     SH_CLERK    3200   NaN  123.0   40.0
96   196        Alana        Walsh    awalsh@gmail.com        650.507.9811  24-04-1998     SH_CLERK    3100   NaN  124.0   40.0
97   197        Kevin       Feeney   kfeeney@gmail.com        650.507.9822  23-05-1998     SH_CLERK    3000   NaN  124.0   40.0
95   195        Vance        Jones    vjones@gmail.com        650.501.4876  17-03-1999     SH_CLERK    2800   NaN  123.0   40.0
21   121         Adam        Fripp    afripp@gmail.com        650.123.2234  10-04-1997       ST_MAN    8200   NaN  100.0   50.0
20   120      Matthew        Weiss    mweiss@gmail.com        650.123.1234  18-07-1996       ST_MAN    8000   NaN  100.0   50.0
22   122        Payam     Kaufling  pkauflin@gmail.com        650.123.3234  01-05-1995       ST_MAN    7900   NaN  100.0   50.0
23   123       Shanta      Vollman  svollman@gmail.com        650.123.4234  10-10-1997       ST_MAN    6500   NaN  100.0   50.0
24   124        Kevin      Mourgos  kmourgos@gmail.com        650.123.5234  16-11-1999       ST_MAN    5800   NaN  100.0   50.0
84   184      Nandita     Sarchand  nsarchan@gmail.com        650.509.1876  27-01-1996     SH_CLERK    4200   NaN  121.0   50.0
85   185       Alexis         Bull     abull@gmail.com        650.509.2876  20-02-1997     SH_CLERK    4100   NaN  121.0   50.0
92   192        Sarah         Bell     sbell@gmail.com        650.501.1876  04-02-1996     SH_CLERK    4000   NaN  123.0   50.0
93   193      Britney      Everett  beverett@gmail.com        650.501.2876  03-03-1997     SH_CLERK    3900   NaN  123.0   50.0
88   188        Kelly        Chung    kchung@gmail.com        650.505.1876  14-06-1997     SH_CLERK    3800   NaN  122.0   50.0
37   137       Renske       Ladwig   rladwig@gmail.com        650.121.1234  14-07-1995     ST_CLERK    3600   NaN  123.0   50.0
89   189     Jennifer        Dilly    jdilly@gmail.com        650.505.2876  13-08-1997     SH_CLERK    3600   NaN  122.0   50.0
86   186        Julia    Dellinger  jdelling@gmail.com        650.509.3876  24-06-1998     SH_CLERK    3400   NaN  121.0   50.0
29   129        Laura       Bissot   lbissot@gmail.com        650.124.5234  20-08-1997     ST_CLERK    3300   NaN  121.0   50.0
33   133        Jason       Mallin   jmallin@gmail.com        650.127.1934  14-06-1996     ST_CLERK    3300   NaN  122.0   50.0
25   125        Julia        Nayer    jnayer@gmail.com        650.124.1214  16-07-1997     ST_CLERK    3200   NaN  120.0   50.0
38   138      Stephen       Stiles   sstiles@gmail.com        650.121.2034  26-10-1997     ST_CLERK    3200   NaN  123.0   50.0
80   180      Winston       Taylor   wtaylor@gmail.com        650.507.9876  24-01-1998     SH_CLERK    3200   NaN  120.0   50.0
42   142       Curtis       Davies   cdavies@gmail.com        650.121.2994  29-01-1997     ST_CLERK    3100   NaN  124.0   50.0
81   181         Jean       Fleaur   jfleaur@gmail.com        650.507.9877  23-02-1998     SH_CLERK    3100   NaN  120.0   50.0
87   187      Anthony       Cabrio   acabrio@gmail.com        650.509.4876  07-02-1999     SH_CLERK    3000   NaN  121.0   50.0
34   134      Michael       Rogers   mrogers@gmail.com        650.127.1834  26-08-1998     ST_CLERK    2900   NaN  122.0   50.0
90   190      Timothy        Gates    tgates@gmail.com        650.505.3876  11-07-1998     SH_CLERK    2900   NaN  122.0   50.0
30   130        Mozhe     Atkinson  matkinso@gmail.com        650.124.6234  30-10-1997     ST_CLERK    2800   NaN  121.0   50.0
83   183       Girard        Geoni    ggeoni@gmail.com        650.507.9879  03-02-2000     SH_CLERK    2800   NaN  120.0   50.0
26   126        Irene  Mikkilineni  imikkili@gmail.com        650.124.1224  28-09-1998     ST_CLERK    2700   NaN  120.0   50.0
39   139         John          Seo      jseo@gmail.com        650.121.2019  12-02-1998     ST_CLERK    2700   NaN  123.0   50.0
43   143      Randall        Matos    rmatos@gmail.com        650.121.2874  15-03-1998     ST_CLERK    2600   NaN  124.0   50.0
98   198       Donald     OConnell  doconnel@gmail.com        650.507.9833  21-06-1999     SH_CLERK    2600   NaN  124.0   50.0
99   199      Douglas        Grant    dgrant@gmail.com        650.507.9844  13-01-2000     SH_CLERK    2600   NaN  124.0   50.0
31   131        James       Marlow   jamrlow@gmail.com        650.124.7234  16-02-1997     ST_CLERK    2500   NaN  121.0   50.0
44   144        Peter       Vargas   pvargas@gmail.com        650.121.2004  09-07-1998     ST_CLERK    2500   NaN  124.0   50.0
82   182       Martha     Sullivan  msulliva@gmail.com        650.507.9878  21-06-1999     SH_CLERK    2500   NaN  120.0   50.0
91   191      Randall      Perkins  rperkins@gmail.com        650.505.4876  19-12-1999     SH_CLERK    2500   NaN  122.0   50.0
27   127        James       Landry   jlandry@gmail.com        650.124.1334  14-01-1999     ST_CLERK    2400   NaN  120.0   50.0
35   135           Ki          Gee      kgee@gmail.com        650.127.1734  12-12-1999     ST_CLERK    2400   NaN  122.0   50.0
28   128       Steven       Markle   smarkle@gmail.com        650.124.1434  08-03-2000     ST_CLERK    2200   NaN  120.0   50.0
36   136        Hazel   Philtanker  hphiltan@gmail.com        650.127.1634  06-02-2000     ST_CLERK    2200   NaN  122.0   50.0
32   132           TJ        Olson   tjolson@gmail.com        650.124.8234  10-04-1999     ST_CLERK    2100   NaN  121.0   50.0
3    103    Alexander       Hunold   ahunold@gmail.com        590.423.4567  03-01-1990      IT_PROG    9000   NaN  102.0   60.0
4    104        Bruce        Ernst    bernst@gmail.com        590.423.4568  21-05-1991      IT_PROG    6000   NaN  103.0   60.0
5    105        David       Austin   daustin@gmail.com        590.423.4569  25-06-1997      IT_PROG    4800   NaN  103.0   60.0
6    106        Valli    Pataballa  vpatabal@gmail.com        590.423.4560  05-02-1998      IT_PROG    4800   NaN  103.0   60.0
7    107        Diana      Lorentz  dlorentz@gmail.com        590.423.5567  07-02-1999      IT_PROG    4200   NaN  103.0   60.0
45   145         John      Russell   jrussel@gmail.com  011.44.1344.429268  01-10-1996       SA_MAN   14000  0.40  100.0   80.0
46   146        Karen     Partners  kpartner@gmail.com  011.44.1344.467268  05-01-1997       SA_MAN   13500  0.30  100.0   80.0
47   147      Alberto    Errazuriz  aerrazur@gmail.com  011.44.1344.429278  10-03-1997       SA_MAN   12000  0.30  100.0   80.0
68   168         Lisa         Ozer     lozer@gmail.com  011.44.1343.929268  11-03-1997       SA_REP   11500  0.25  148.0   80.0
48   148       Gerald    Cambrault  gcambrau@gmail.com  011.44.1344.619268  15-10-1999       SA_MAN   11000  0.30  100.0   80.0
74   174        Ellen         Abel     eabel@gmail.com  011.44.1644.429267  11-05-1996       SA_REP   11000  0.30  149.0   80.0
49   149        Eleni      Zlotkey  ezlotkey@gmail.com  011.44.1344.429018  29-01-2000       SA_MAN   10500  0.20  100.0   80.0
62   162        Clara      Vishney  cvishney@gmail.com  011.44.1346.129268  11-11-1997       SA_REP   10500  0.25  147.0   80.0
50   150        Peter       Tucker   ptucker@gmail.com  011.44.1344.129268  30-01-1997       SA_REP   10000  0.30  145.0   80.0
56   156      Janette         King     jking@gmail.com  011.44.1345.429268  30-01-1996       SA_REP   10000  0.35  146.0   80.0
69   169     Harrison        Bloom    hbloom@gmail.com  011.44.1343.829268  23-03-1998       SA_REP   10000  0.20  148.0   80.0
70   170       Tayler          Fox      tfox@gmail.com  011.44.1343.729268  24-01-1998       SA_REP    9600  0.20  148.0   80.0
51   151        David    Bernstein  dbernste@gmail.com  011.44.1344.345268  24-03-1997       SA_REP    9500  0.25  145.0   80.0
57   157      Patrick        Sully    psully@gmail.com  011.44.1345.929268  04-03-1996       SA_REP    9500  0.35  146.0   80.0
63   163     Danielle       Greene   dgreene@gmail.com  011.44.1346.229268  19-03-1999       SA_REP    9500  0.15  147.0   80.0
52   152        Peter         Hall     phall@gmail.com  011.44.1344.478968  20-08-1997       SA_REP    9000  0.25  145.0   80.0
58   158        Allan       McEwen   amcewen@gmail.com  011.44.1345.829268  01-08-1996       SA_REP    9000  0.35  146.0   80.0
75   175       Alyssa       Hutton   ahutton@gmail.com  011.44.1644.429266  19-03-1997       SA_REP    8800  0.25  149.0   80.0
76   176     Jonathon       Taylor   jtaylor@gmail.com  011.44.1644.429265  24-03-1998       SA_REP    8600  0.20  149.0   80.0
77   177         Jack   Livingston  jlivings@gmail.com  011.44.1644.429264  23-04-1998       SA_REP    8400  0.20  149.0   80.0
53   153  Christopher        Olsen    colsen@gmail.com  011.44.1344.498718  30-03-1998       SA_REP    8000  0.20  145.0   80.0
59   159      Lindsey        Smith    lsmith@gmail.com  011.44.1345.729268  10-03-1997       SA_REP    8000  0.30  146.0   80.0
54   154      Nanette    Cambrault  ncambrau@gmail.com  011.44.1344.987668  09-12-1998       SA_REP    7500  0.20  145.0   80.0
60   160       Louise        Doran    ldoran@gmail.com  011.44.1345.629268  15-12-1997       SA_REP    7500  0.30  146.0   80.0
71   171      William        Smith    wsmith@gmail.com  011.44.1343.629268  23-02-1999       SA_REP    7400  0.15  148.0   80.0
72   172    Elizabeth        Bates    ebates@gmail.com  011.44.1343.529268  24-03-1999       SA_REP    7300  0.15  148.0   80.0
64   164       Mattea      Marvins  mmarvins@gmail.com  011.44.1346.329268  24-01-2000       SA_REP    7200  0.10  147.0   80.0
55   155       Oliver      Tuvault  otuvault@gmail.com  011.44.1344.486508  23-11-1999       SA_REP    7000  0.15  145.0   80.0
61   161       Sarath       Sewall   ssewall@gmail.com  011.44.1345.529268  03-11-1998       SA_REP    7000  0.25  146.0   80.0
65   165        David          Lee      dlee@gmail.com  011.44.1346.529268  23-02-2000       SA_REP    6800  0.10  147.0   80.0
66   166       Sundar         Ande     sande@gmail.com  011.44.1346.629268  24-03-2000       SA_REP    6400  0.10  147.0   80.0
67   167         Amit        Banda    abanda@gmail.com  011.44.1346.729268  21-04-2000       SA_REP    6200  0.10  147.0   80.0
79   179      Charles      Johnson  cjohnson@gmail.com  011.44.1644.429262  04-01-2000       SA_REP    6200  0.10  149.0   80.0
73   173      Sundita        Kumar    skumar@gmail.com  011.44.1343.329268  21-04-2000       SA_REP    6100  0.10  148.0   80.0
0    100       Steven         King     sking@gmail.com        515.123.4567  17-06-1987      AD_PRES   24000   NaN    NaN   90.0
1    101        Neena      Kochhar  nkochhar@gmail.com        515.123.4568  21-09-1989        AD_VP   17000   NaN  100.0   90.0
2    102          Lex      De Haan   ldehaan@gmail.com        515.123.4569  13-01-1993        AD_VP   17000   NaN  100.0   90.0
8    108        Nancy    Greenberg  ngreenbe@gmail.com        515.124.4569  17-08-1994       FI_MGR   12000   NaN  101.0  100.0
9    109       Daniel       Faviet   dfaviet@gmail.com        515.124.4169  16-08-1994   FI_ACCOUNT    9000   NaN  108.0  100.0
10   110         John         Chen     jchen@gmail.com        515.124.4269  28-09-1997   FI_ACCOUNT    8200   NaN  108.0  100.0
12   112  Jose Manuel        Urman   jmurman@gmail.com        515.124.4469  07-03-1998   FI_ACCOUNT    7800   NaN  108.0  100.0
11   111       Ismael      Sciarra  isciarra@gmail.com        515.124.4369  30-09-1997   FI_ACCOUNT    7700   NaN  108.0  100.0
13   113         Luis         Popp     lpopp@gmail.com        515.124.4567  07-12-1999   FI_ACCOUNT    6900   NaN  108.0  100.0
78   178    Kimberely        Grant    kgrant@gmail.com  011.44.1644.429263  24-05-1999       SA_REP    7000  0.15  149.0    NaN
>>> (res.sort_values(by=['did','salary'],ascending=[True,False]))['did']
100     10.0
41      20.0
40      20.0
14      30.0
15      30.0
16      30.0
17      30.0
18      30.0
19      30.0
94      40.0
96      40.0
97      40.0
95      40.0
21      50.0
20      50.0
22      50.0
23      50.0
24      50.0
84      50.0
85      50.0
92      50.0
93      50.0
88      50.0
37      50.0
89      50.0
86      50.0
29      50.0
33      50.0
25      50.0
38      50.0
80      50.0
42      50.0
81      50.0
87      50.0
34      50.0
90      50.0
30      50.0
83      50.0
26      50.0
39      50.0
43      50.0
98      50.0
99      50.0
31      50.0
44      50.0
82      50.0
91      50.0
27      50.0
35      50.0
28      50.0
36      50.0
32      50.0
3       60.0
4       60.0
5       60.0
6       60.0
7       60.0
45      80.0
46      80.0
47      80.0
68      80.0
48      80.0
74      80.0
49      80.0
62      80.0
50      80.0
56      80.0
69      80.0
70      80.0
51      80.0
57      80.0
63      80.0
52      80.0
58      80.0
75      80.0
76      80.0
77      80.0
53      80.0
59      80.0
54      80.0
60      80.0
71      80.0
72      80.0
64      80.0
55      80.0
61      80.0
65      80.0
66      80.0
67      80.0
79      80.0
73      80.0
0       90.0
1       90.0
2       90.0
8      100.0
9      100.0
10     100.0
12     100.0
11     100.0
13     100.0
78       NaN
Name: did, dtype: float64
>>> (res.sort_values(by=['did','salary'],ascending=[True,False]))[["did","salary"]]
       did  salary
100   10.0    4400
41    20.0    3500
40    20.0    2500
14    30.0   11000
15    30.0    3100
16    30.0    2900
17    30.0    2800
18    30.0    2600
19    30.0    2500
94    40.0    3200
96    40.0    3100
97    40.0    3000
95    40.0    2800
21    50.0    8200
20    50.0    8000
22    50.0    7900
23    50.0    6500
24    50.0    5800
84    50.0    4200
85    50.0    4100
92    50.0    4000
93    50.0    3900
88    50.0    3800
37    50.0    3600
89    50.0    3600
86    50.0    3400
29    50.0    3300
33    50.0    3300
25    50.0    3200
38    50.0    3200
80    50.0    3200
42    50.0    3100
81    50.0    3100
87    50.0    3000
34    50.0    2900
90    50.0    2900
30    50.0    2800
83    50.0    2800
26    50.0    2700
39    50.0    2700
43    50.0    2600
98    50.0    2600
99    50.0    2600
31    50.0    2500
44    50.0    2500
82    50.0    2500
91    50.0    2500
27    50.0    2400
35    50.0    2400
28    50.0    2200
36    50.0    2200
32    50.0    2100
3     60.0    9000
4     60.0    6000
5     60.0    4800
6     60.0    4800
7     60.0    4200
45    80.0   14000
46    80.0   13500
47    80.0   12000
68    80.0   11500
48    80.0   11000
74    80.0   11000
49    80.0   10500
62    80.0   10500
50    80.0   10000
56    80.0   10000
69    80.0   10000
70    80.0    9600
51    80.0    9500
57    80.0    9500
63    80.0    9500
52    80.0    9000
58    80.0    9000
75    80.0    8800
76    80.0    8600
77    80.0    8400
53    80.0    8000
59    80.0    8000
54    80.0    7500
60    80.0    7500
71    80.0    7400
72    80.0    7300
64    80.0    7200
55    80.0    7000
61    80.0    7000
65    80.0    6800
66    80.0    6400
67    80.0    6200
79    80.0    6200
73    80.0    6100
0     90.0   24000
1     90.0   17000
2     90.0   17000
8    100.0   12000
9    100.0    9000
10   100.0    8200
12   100.0    7800
11   100.0    7700
13   100.0    6900
78     NaN    7000
>>> 16    30.0    2900
SyntaxError: invalid syntax
>>> res[0:3]
   eid   fname    lname               email         phone     hiredate    jobid  salary  comm    mid   did
0  100  Steven     King     sking@gmail.com  515.123.4567  17-06-1987   AD_PRES   24000   NaN    NaN  90.0
1  101   Neena  Kochhar  nkochhar@gmail.com  515.123.4568  21-09-1989     AD_VP   17000   NaN  100.0  90.0
2  102     Lex  De Haan   ldehaan@gmail.com  515.123.4569  13-01-1993     AD_VP   17000   NaN  100.0  90.0
>>> res[0:3,['fname','salary']]
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    res[0:3,['fname','salary']]
  File "C:\Python37\lib\site-packages\pandas\core\frame.py", line 2995, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Python37\lib\site-packages\pandas\core\indexes\base.py", line 2897, in get_loc
    return self._engine.get_loc(key)
  File "pandas/_libs/index.pyx", line 107, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 109, in pandas._libs.index.IndexEngine.get_loc
TypeError: '(slice(0, 3, None), ['fname', 'salary'])' is an invalid key
>>> res.loc[0:3,['fname','salary']]
       fname  salary
0     Steven   24000
1      Neena   17000
2        Lex   17000
3  Alexander    9000
>>> #in case of res.loc the 'end' is inclusive i.e. 3 will also be included
>>> 
>>> 
>>> 
>>> EMS=pd.Excel('C://Python37//Prog//files//EMS.xlsx')
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    EMS=pd.Excel('C://Python37//Prog//files//EMS.xlsx')
  File "C:\Python37\lib\site-packages\pandas\__init__.py", line 214, in __getattr__
    raise AttributeError("module 'pandas' has no attribute '{}'".format(name))
AttributeError: module 'pandas' has no attribute 'Excel'
>>> import xlrd
>>> import openpyexcel
>>> 
>>> EMS=pd.Excel('C://Python37//Prog//files//EMS.xlsx')
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    EMS=pd.Excel('C://Python37//Prog//files//EMS.xlsx')
  File "C:\Python37\lib\site-packages\pandas\__init__.py", line 214, in __getattr__
    raise AttributeError("module 'pandas' has no attribute '{}'".format(name))
AttributeError: module 'pandas' has no attribute 'Excel'
>>> import pandas aspd
SyntaxError: invalid syntax
>>> import pandas as pd
>>> EMS=pd.Excel('C://Python37//Prog//files//EMS.xlsx')
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    EMS=pd.Excel('C://Python37//Prog//files//EMS.xlsx')
  File "C:\Python37\lib\site-packages\pandas\__init__.py", line 214, in __getattr__
    raise AttributeError("module 'pandas' has no attribute '{}'".format(name))
AttributeError: module 'pandas' has no attribute 'Excel'
>>> EMS=pd.ExcelFile('C://Python37//Prog//files//EMS.xlsx')
>>> 
>>> emp=pd.read_excel(EMS,'Sheet1')
>>> dpt=pd.read_excel(EMS,'Sheet2')
>>> loc=pd.read_excel(EMS,'Sheet3')
>>> emp

>>> dpt
    Department_Id       Department_Name  Manager_Id  Location_Id
0              10        Administration       200.0         1700
1              20             Marketing       201.0         1800
2              30            Purchasing       114.0         1700
3              40       Human Resources       203.0         2400
4              50              Shipping       121.0         1500
5              60                    IT       103.0         1400
6              70      Public Relations       204.0         2700
7              80                 Sales       145.0         2500
8              90             Executive       100.0         1700
9             100               Finance       108.0         1700
10            110            Accounting       205.0         1700
11            120              Treasury         NaN         1700
12            130         Corporate Tax         NaN         1700
13            140    Control And Credit         NaN         1700
14            150  Shareholder Services         NaN         1700
15            160              Benefits         NaN         1700
16            170         Manufacturing         NaN         1700
17            180          Construction         NaN         1700
18            190           Contracting         NaN         1700
19            200            Operations         NaN         1700
20            210            IT Support         NaN         1700
21            220                   NOC         NaN         1700
22            230           IT Helpdesk         NaN         1700
23            240      Government Sales         NaN         1700
24            250          Retail Sales         NaN         1700
25            260            Recruiting         NaN         1700
26            270               Payroll         NaN         1700
>>> loc
    Location_Id             Street_Address               Postal_Code                 City    State_Province Country_Id
0          1000       1297 Via Cola di Rie                       989                 Roma               NaN         IT
1          1100    93091 Calle della Testa                     10934               Venice               NaN         IT
2          1200           2017 Shinjuku-ku                      1689                Tokyo  Tokyo Prefecture         JP
3          1300            9450 Kamiya-cho                      6823            Hiroshima               NaN         JP
4          1400        2014 Jabberwocky Rd                     26192            Southlake             Texas         US
5          1500        2011 Interiors Blvd                     99236  South San Francisco        California         US
6          1600             2007 Zagora St                     50090      South Brunswick        New Jersey         US
7          1700            2004 Charade Rd                     98199              Seattle        Washington         US
8          1800            147 Spadina Ave                   M5V 2L7              Toronto           Ontario         CA
9          1900            6092 Boxwood St                   YSW 9T2           Whitehorse             Yukon         CA
10         2000        40-5-12 Laogianggen                    190518              Beijing               NaN         CN
11         2100         1298 Vileparle (E)                    490231               Bombay       Maharashtra         IN
12         2200      12-98 Victoria Street                      2901               Sydney   New South Wales         AU
13         2300         198 Clementi North                    540198            Singapore               NaN         SG
14         2400             8204 Arthur St                       NaN               London               NaN         UK
15         2500            Magdalen Centre   The Oxford Science Park              OX9 9ZB            Oxford     Oxford
16         2600          9702 Chester Road                9629850293            Stretford        Manchester         UK
17         2700      Schwanthalerstr. 7031                     80925               Munich           Bavaria         DE
18         2800      Rua Frei Caneca 1360                  01307-002            Sao Paulo         Sao Paulo         BR
19         2900    20 Rue des Corps-Saints                      1730               Geneva            Geneve         CH
20         3000          Murtenstrasse 921                      3095                 Bern                BE         CH
21         3100  Pieter Breughelstraat 837                    3029SK              Utrecht           Utrecht         NL
22         3200      Mariano Escobedo 9991                     11932          Mexico City  Distrito Federal         MX
>>> 
>>> dpt2=pd.concat([dpt,dpt])
>>> dpt2
    Department_Id       Department_Name  Manager_Id  Location_Id
0              10        Administration       200.0         1700
1              20             Marketing       201.0         1800
2              30            Purchasing       114.0         1700
3              40       Human Resources       203.0         2400
4              50              Shipping       121.0         1500
5              60                    IT       103.0         1400
6              70      Public Relations       204.0         2700
7              80                 Sales       145.0         2500
8              90             Executive       100.0         1700
9             100               Finance       108.0         1700
10            110            Accounting       205.0         1700
11            120              Treasury         NaN         1700
12            130         Corporate Tax         NaN         1700
13            140    Control And Credit         NaN         1700
14            150  Shareholder Services         NaN         1700
15            160              Benefits         NaN         1700
16            170         Manufacturing         NaN         1700
17            180          Construction         NaN         1700
18            190           Contracting         NaN         1700
19            200            Operations         NaN         1700
20            210            IT Support         NaN         1700
21            220                   NOC         NaN         1700
22            230           IT Helpdesk         NaN         1700
23            240      Government Sales         NaN         1700
24            250          Retail Sales         NaN         1700
25            260            Recruiting         NaN         1700
26            270               Payroll         NaN         1700
0              10        Administration       200.0         1700
1              20             Marketing       201.0         1800
2              30            Purchasing       114.0         1700
3              40       Human Resources       203.0         2400
4              50              Shipping       121.0         1500
5              60                    IT       103.0         1400
6              70      Public Relations       204.0         2700
7              80                 Sales       145.0         2500
8              90             Executive       100.0         1700
9             100               Finance       108.0         1700
10            110            Accounting       205.0         1700
11            120              Treasury         NaN         1700
12            130         Corporate Tax         NaN         1700
13            140    Control And Credit         NaN         1700
14            150  Shareholder Services         NaN         1700
15            160              Benefits         NaN         1700
16            170         Manufacturing         NaN         1700
17            180          Construction         NaN         1700
18            190           Contracting         NaN         1700
19            200            Operations         NaN         1700
20            210            IT Support         NaN         1700
21            220                   NOC         NaN         1700
22            230           IT Helpdesk         NaN         1700
23            240      Government Sales         NaN         1700
24            250          Retail Sales         NaN         1700
25            260            Recruiting         NaN         1700
26            270               Payroll         NaN         1700
>>> dpt2=pd.concat([dpt,loc])

Warning (from warnings module):
  File "__main__", line 1
FutureWarning: Sorting because non-concatenation axis is not aligned. A future version
of pandas will change to not sort by default.

To accept the future behavior, pass 'sort=False'.

To retain the current behavior and silence the warning, pass 'sort=True'.

>>> dpt.append(dpt)
    Department_Id       Department_Name  Manager_Id  Location_Id
0              10        Administration       200.0         1700
1              20             Marketing       201.0         1800
2              30            Purchasing       114.0         1700
3              40       Human Resources       203.0         2400
4              50              Shipping       121.0         1500
5              60                    IT       103.0         1400
6              70      Public Relations       204.0         2700
7              80                 Sales       145.0         2500
8              90             Executive       100.0         1700
9             100               Finance       108.0         1700
10            110            Accounting       205.0         1700
11            120              Treasury         NaN         1700
12            130         Corporate Tax         NaN         1700
13            140    Control And Credit         NaN         1700
14            150  Shareholder Services         NaN         1700
15            160              Benefits         NaN         1700
16            170         Manufacturing         NaN         1700
17            180          Construction         NaN         1700
18            190           Contracting         NaN         1700
19            200            Operations         NaN         1700
20            210            IT Support         NaN         1700
21            220                   NOC         NaN         1700
22            230           IT Helpdesk         NaN         1700
23            240      Government Sales         NaN         1700
24            250          Retail Sales         NaN         1700
25            260            Recruiting         NaN         1700
26            270               Payroll         NaN         1700
0              10        Administration       200.0         1700
1              20             Marketing       201.0         1800
2              30            Purchasing       114.0         1700
3              40       Human Resources       203.0         2400
4              50              Shipping       121.0         1500
5              60                    IT       103.0         1400
6              70      Public Relations       204.0         2700
7              80                 Sales       145.0         2500
8              90             Executive       100.0         1700
9             100               Finance       108.0         1700
10            110            Accounting       205.0         1700
11            120              Treasury         NaN         1700
12            130         Corporate Tax         NaN         1700
13            140    Control And Credit         NaN         1700
14            150  Shareholder Services         NaN         1700
15            160              Benefits         NaN         1700
16            170         Manufacturing         NaN         1700
17            180          Construction         NaN         1700
18            190           Contracting         NaN         1700
19            200            Operations         NaN         1700
20            210            IT Support         NaN         1700
21            220                   NOC         NaN         1700
22            230           IT Helpdesk         NaN         1700
23            240      Government Sales         NaN         1700
24            250          Retail Sales         NaN         1700
25            260            Recruiting         NaN         1700
26            270               Payroll         NaN         1700
>>> 
>>> pd.concat([dpt,dpt],axis=1)
    Department_Id       Department_Name  Manager_Id  Location_Id  Department_Id       Department_Name  Manager_Id  Location_Id
0              10        Administration       200.0         1700             10        Administration       200.0         1700
1              20             Marketing       201.0         1800             20             Marketing       201.0         1800
2              30            Purchasing       114.0         1700             30            Purchasing       114.0         1700
3              40       Human Resources       203.0         2400             40       Human Resources       203.0         2400
4              50              Shipping       121.0         1500             50              Shipping       121.0         1500
5              60                    IT       103.0         1400             60                    IT       103.0         1400
6              70      Public Relations       204.0         2700             70      Public Relations       204.0         2700
7              80                 Sales       145.0         2500             80                 Sales       145.0         2500
8              90             Executive       100.0         1700             90             Executive       100.0         1700
9             100               Finance       108.0         1700            100               Finance       108.0         1700
10            110            Accounting       205.0         1700            110            Accounting       205.0         1700
11            120              Treasury         NaN         1700            120              Treasury         NaN         1700
12            130         Corporate Tax         NaN         1700            130         Corporate Tax         NaN         1700
13            140    Control And Credit         NaN         1700            140    Control And Credit         NaN         1700
14            150  Shareholder Services         NaN         1700            150  Shareholder Services         NaN         1700
15            160              Benefits         NaN         1700            160              Benefits         NaN         1700
16            170         Manufacturing         NaN         1700            170         Manufacturing         NaN         1700
17            180          Construction         NaN         1700            180          Construction         NaN         1700
18            190           Contracting         NaN         1700            190           Contracting         NaN         1700
19            200            Operations         NaN         1700            200            Operations         NaN         1700
20            210            IT Support         NaN         1700            210            IT Support         NaN         1700
21            220                   NOC         NaN         1700            220                   NOC         NaN         1700
22            230           IT Helpdesk         NaN         1700            230           IT Helpdesk         NaN         1700
23            240      Government Sales         NaN         1700            240      Government Sales         NaN         1700
24            250          Retail Sales         NaN         1700            250          Retail Sales         NaN         1700
25            260            Recruiting         NaN         1700            260            Recruiting         NaN         1700
26            270               Payroll         NaN         1700            270               Payroll         NaN         1700
>>> dpt
    Department_Id       Department_Name  Manager_Id  Location_Id
0              10        Administration       200.0         1700
1              20             Marketing       201.0         1800
2              30            Purchasing       114.0         1700
3              40       Human Resources       203.0         2400
4              50              Shipping       121.0         1500
5              60                    IT       103.0         1400
6              70      Public Relations       204.0         2700
7              80                 Sales       145.0         2500
8              90             Executive       100.0         1700
9             100               Finance       108.0         1700
10            110            Accounting       205.0         1700
11            120              Treasury         NaN         1700
12            130         Corporate Tax         NaN         1700
13            140    Control And Credit         NaN         1700
14            150  Shareholder Services         NaN         1700
15            160              Benefits         NaN         1700
16            170         Manufacturing         NaN         1700
17            180          Construction         NaN         1700
18            190           Contracting         NaN         1700
19            200            Operations         NaN         1700
20            210            IT Support         NaN         1700
21            220                   NOC         NaN         1700
22            230           IT Helpdesk         NaN         1700
23            240      Government Sales         NaN         1700
24            250          Retail Sales         NaN         1700
25            260            Recruiting         NaN         1700
26            270               Payroll         NaN         1700
>>> 
>>> pd.merge(dpt,loc,on='Location_Id')
    Department_Id       Department_Name  Manager_Id  Location_Id         Street_Address               Postal_Code                 City State_Province Country_Id
0              10        Administration       200.0         1700        2004 Charade Rd                     98199              Seattle     Washington         US
1              30            Purchasing       114.0         1700        2004 Charade Rd                     98199              Seattle     Washington         US
2              90             Executive       100.0         1700        2004 Charade Rd                     98199              Seattle     Washington         US
3             100               Finance       108.0         1700        2004 Charade Rd                     98199              Seattle     Washington         US
4             110            Accounting       205.0         1700        2004 Charade Rd                     98199              Seattle     Washington         US
5             120              Treasury         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
6             130         Corporate Tax         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
7             140    Control And Credit         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
8             150  Shareholder Services         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
9             160              Benefits         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
10            170         Manufacturing         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
11            180          Construction         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
12            190           Contracting         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
13            200            Operations         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
14            210            IT Support         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
15            220                   NOC         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
16            230           IT Helpdesk         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
17            240      Government Sales         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
18            250          Retail Sales         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
19            260            Recruiting         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
20            270               Payroll         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
21             20             Marketing       201.0         1800        147 Spadina Ave                   M5V 2L7              Toronto        Ontario         CA
22             40       Human Resources       203.0         2400         8204 Arthur St                       NaN               London            NaN         UK
23             50              Shipping       121.0         1500    2011 Interiors Blvd                     99236  South San Francisco     California         US
24             60                    IT       103.0         1400    2014 Jabberwocky Rd                     26192            Southlake          Texas         US
25             70      Public Relations       204.0         2700  Schwanthalerstr. 7031                     80925               Munich        Bavaria         DE
26             80                 Sales       145.0         2500        Magdalen Centre   The Oxford Science Park              OX9 9ZB         Oxford     Oxford
>>> # Above command is used to merge two dataframe based on an attribute
>>> 
>>> pd.merge(dpt,loc,on='Location_Id',how='left')
    Department_Id       Department_Name  Manager_Id  Location_Id         Street_Address               Postal_Code                 City State_Province Country_Id
0              10        Administration       200.0         1700        2004 Charade Rd                     98199              Seattle     Washington         US
1              20             Marketing       201.0         1800        147 Spadina Ave                   M5V 2L7              Toronto        Ontario         CA
2              30            Purchasing       114.0         1700        2004 Charade Rd                     98199              Seattle     Washington         US
3              40       Human Resources       203.0         2400         8204 Arthur St                       NaN               London            NaN         UK
4              50              Shipping       121.0         1500    2011 Interiors Blvd                     99236  South San Francisco     California         US
5              60                    IT       103.0         1400    2014 Jabberwocky Rd                     26192            Southlake          Texas         US
6              70      Public Relations       204.0         2700  Schwanthalerstr. 7031                     80925               Munich        Bavaria         DE
7              80                 Sales       145.0         2500        Magdalen Centre   The Oxford Science Park              OX9 9ZB         Oxford     Oxford
8              90             Executive       100.0         1700        2004 Charade Rd                     98199              Seattle     Washington         US
9             100               Finance       108.0         1700        2004 Charade Rd                     98199              Seattle     Washington         US
10            110            Accounting       205.0         1700        2004 Charade Rd                     98199              Seattle     Washington         US
11            120              Treasury         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
12            130         Corporate Tax         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
13            140    Control And Credit         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
14            150  Shareholder Services         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
15            160              Benefits         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
16            170         Manufacturing         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
17            180          Construction         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
18            190           Contracting         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
19            200            Operations         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
20            210            IT Support         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
21            220                   NOC         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
22            230           IT Helpdesk         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
23            240      Government Sales         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
24            250          Retail Sales         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
25            260            Recruiting         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
26            270               Payroll         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
>>> pd.merge(dpt,loc,on='Location_Id',how='left',suffixes=('_left','_right'))
    Department_Id       Department_Name  Manager_Id  Location_Id         Street_Address               Postal_Code                 City State_Province Country_Id
0              10        Administration       200.0         1700        2004 Charade Rd                     98199              Seattle     Washington         US
1              20             Marketing       201.0         1800        147 Spadina Ave                   M5V 2L7              Toronto        Ontario         CA
2              30            Purchasing       114.0         1700        2004 Charade Rd                     98199              Seattle     Washington         US
3              40       Human Resources       203.0         2400         8204 Arthur St                       NaN               London            NaN         UK
4              50              Shipping       121.0         1500    2011 Interiors Blvd                     99236  South San Francisco     California         US
5              60                    IT       103.0         1400    2014 Jabberwocky Rd                     26192            Southlake          Texas         US
6              70      Public Relations       204.0         2700  Schwanthalerstr. 7031                     80925               Munich        Bavaria         DE
7              80                 Sales       145.0         2500        Magdalen Centre   The Oxford Science Park              OX9 9ZB         Oxford     Oxford
8              90             Executive       100.0         1700        2004 Charade Rd                     98199              Seattle     Washington         US
9             100               Finance       108.0         1700        2004 Charade Rd                     98199              Seattle     Washington         US
10            110            Accounting       205.0         1700        2004 Charade Rd                     98199              Seattle     Washington         US
11            120              Treasury         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
12            130         Corporate Tax         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
13            140    Control And Credit         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
14            150  Shareholder Services         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
15            160              Benefits         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
16            170         Manufacturing         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
17            180          Construction         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
18            190           Contracting         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
19            200            Operations         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
20            210            IT Support         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
21            220                   NOC         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
22            230           IT Helpdesk         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
23            240      Government Sales         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
24            250          Retail Sales         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
25            260            Recruiting         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
26            270               Payroll         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
>>> pd.merge(dpt,loc,on='Location_Id',how='inner',suffixes=('_left','_right'))
    Department_Id       Department_Name  Manager_Id  Location_Id         Street_Address               Postal_Code                 City State_Province Country_Id
0              10        Administration       200.0         1700        2004 Charade Rd                     98199              Seattle     Washington         US
1              30            Purchasing       114.0         1700        2004 Charade Rd                     98199              Seattle     Washington         US
2              90             Executive       100.0         1700        2004 Charade Rd                     98199              Seattle     Washington         US
3             100               Finance       108.0         1700        2004 Charade Rd                     98199              Seattle     Washington         US
4             110            Accounting       205.0         1700        2004 Charade Rd                     98199              Seattle     Washington         US
5             120              Treasury         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
6             130         Corporate Tax         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
7             140    Control And Credit         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
8             150  Shareholder Services         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
9             160              Benefits         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
10            170         Manufacturing         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
11            180          Construction         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
12            190           Contracting         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
13            200            Operations         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
14            210            IT Support         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
15            220                   NOC         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
16            230           IT Helpdesk         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
17            240      Government Sales         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
18            250          Retail Sales         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
19            260            Recruiting         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
20            270               Payroll         NaN         1700        2004 Charade Rd                     98199              Seattle     Washington         US
21             20             Marketing       201.0         1800        147 Spadina Ave                   M5V 2L7              Toronto        Ontario         CA
22             40       Human Resources       203.0         2400         8204 Arthur St                       NaN               London            NaN         UK
23             50              Shipping       121.0         1500    2011 Interiors Blvd                     99236  South San Francisco     California         US
24             60                    IT       103.0         1400    2014 Jabberwocky Rd                     26192            Southlake          Texas         US
25             70      Public Relations       204.0         2700  Schwanthalerstr. 7031                     80925               Munich        Bavaria         DE
26             80                 Sales       145.0         2500        Magdalen Centre   The Oxford Science Park              OX9 9ZB         Oxford     Oxford
>>> pd.merge(dpt,emp,on='Department_Id',how='right',suffixes=('_left','_right'))
     Department_Id   Department_Name  Manager_Id_left  Location_Id  Employee_Id         Name  Hire_Date      Job_Id  Salary  Manager_Id_right
0             10.0    Administration            200.0       1700.0          200     Jennifer 1987-09-17     AD_ASST    4400             101.0
1             20.0         Marketing            201.0       1800.0          201      Michael 1996-02-17      MK_MAN   13000             100.0
2             20.0         Marketing            201.0       1800.0          202          Pat 1997-08-17      MK_REP    6000             201.0
3             30.0        Purchasing            114.0       1700.0          114          Den 1994-12-07      PU_MAN   11000             100.0
4             30.0        Purchasing            114.0       1700.0          115    Alexander 1995-05-18    PU_CLERK    3100             114.0
5             30.0        Purchasing            114.0       1700.0          116       Shelli 1997-12-24    PU_CLERK    2900             114.0
6             30.0        Purchasing            114.0       1700.0          117        Sigal 1997-07-24    PU_CLERK    2800             114.0
7             30.0        Purchasing            114.0       1700.0          118          Guy 1998-11-15    PU_CLERK    2600             114.0
8             30.0        Purchasing            114.0       1700.0          119        Karen 1999-08-10    PU_CLERK    2500             114.0
9             40.0   Human Resources            203.0       2400.0          203        Susan 1994-06-07      HR_REP    6500             101.0
10            50.0          Shipping            121.0       1500.0          120      Matthew 1996-07-18      ST_MAN    8000             100.0
11            50.0          Shipping            121.0       1500.0          121         Adam 1997-04-10      ST_MAN    8200             100.0
12            50.0          Shipping            121.0       1500.0          122        Payam 1995-05-01      ST_MAN    7900             100.0
13            50.0          Shipping            121.0       1500.0          123       Shanta 1997-10-10      ST_MAN    6500             100.0
14            50.0          Shipping            121.0       1500.0          124        Kevin 1999-11-16      ST_MAN    5800             100.0
15            50.0          Shipping            121.0       1500.0          125        Julia 1997-07-16    ST_CLERK    3200             120.0
16            50.0          Shipping            121.0       1500.0          126        Irene 1998-09-28    ST_CLERK    2700             120.0
17            50.0          Shipping            121.0       1500.0          127        James 1999-01-14    ST_CLERK    2400             120.0
18            50.0          Shipping            121.0       1500.0          128       Steven 2000-03-08    ST_CLERK    2200             120.0
19            50.0          Shipping            121.0       1500.0          129        Laura 1997-08-20    ST_CLERK    3300             121.0
20            50.0          Shipping            121.0       1500.0          130        Mozhe 1997-10-30    ST_CLERK    2800             121.0
21            50.0          Shipping            121.0       1500.0          131        James 1997-02-16    ST_CLERK    2500             121.0
22            50.0          Shipping            121.0       1500.0          132           TJ 1999-04-10    ST_CLERK    2100             121.0
23            50.0          Shipping            121.0       1500.0          133        Jason 1996-06-14    ST_CLERK    3300             122.0
24            50.0          Shipping            121.0       1500.0          134      Michael 1998-08-26    ST_CLERK    2900             122.0
25            50.0          Shipping            121.0       1500.0          135           Ki 1999-12-12    ST_CLERK    2400             122.0
26            50.0          Shipping            121.0       1500.0          136        Hazel 2000-02-06    ST_CLERK    2200             122.0
27            50.0          Shipping            121.0       1500.0          137       Renske 1995-07-14    ST_CLERK    3600             123.0
28            50.0          Shipping            121.0       1500.0          138      Stephen 1997-10-26    ST_CLERK    3200             123.0
29            50.0          Shipping            121.0       1500.0          139         John 1998-02-12    ST_CLERK    2700             123.0
30            50.0          Shipping            121.0       1500.0          140       Joshua 1998-04-06    ST_CLERK    2500             123.0
31            50.0          Shipping            121.0       1500.0          141       Trenna 1995-10-17    ST_CLERK    3500             124.0
32            50.0          Shipping            121.0       1500.0          142       Curtis 1997-01-29    ST_CLERK    3100             124.0
33            50.0          Shipping            121.0       1500.0          143      Randall 1998-03-15    ST_CLERK    2600             124.0
34            50.0          Shipping            121.0       1500.0          144        Peter 1998-07-09    ST_CLERK    2500             124.0
35            50.0          Shipping            121.0       1500.0          180      Winston 1998-01-24    SH_CLERK    3200             120.0
36            50.0          Shipping            121.0       1500.0          181         Jean 1998-02-23    SH_CLERK    3100             120.0
37            50.0          Shipping            121.0       1500.0          182       Martha 1999-06-21    SH_CLERK    2500             120.0
38            50.0          Shipping            121.0       1500.0          183       Girard 2000-02-03    SH_CLERK    2800             120.0
39            50.0          Shipping            121.0       1500.0          184      Nandita 1996-01-27    SH_CLERK    4200             121.0
40            50.0          Shipping            121.0       1500.0          185       Alexis 1997-02-20    SH_CLERK    4100             121.0
41            50.0          Shipping            121.0       1500.0          186        Julia 1998-06-24    SH_CLERK    3400             121.0
42            50.0          Shipping            121.0       1500.0          187      Anthony 1999-02-07    SH_CLERK    3000             121.0
43            50.0          Shipping            121.0       1500.0          188        Kelly 1997-06-14    SH_CLERK    3800             122.0
44            50.0          Shipping            121.0       1500.0          189     Jennifer 1997-08-13    SH_CLERK    3600             122.0
45            50.0          Shipping            121.0       1500.0          190      Timothy 1998-07-11    SH_CLERK    2900             122.0
46            50.0          Shipping            121.0       1500.0          191      Randall 1999-12-19    SH_CLERK    2500             122.0
47            50.0          Shipping            121.0       1500.0          192        Sarah 1996-02-04    SH_CLERK    4000             123.0
48            50.0          Shipping            121.0       1500.0          193      Britney 1997-03-03    SH_CLERK    3900             123.0
49            50.0          Shipping            121.0       1500.0          194       Samuel 1998-07-01    SH_CLERK    3200             123.0
50            50.0          Shipping            121.0       1500.0          195        Vance 1999-03-17    SH_CLERK    2800             123.0
51            50.0          Shipping            121.0       1500.0          196        Alana 1998-04-24    SH_CLERK    3100             124.0
52            50.0          Shipping            121.0       1500.0          197        Kevin 1998-05-23    SH_CLERK    3000             124.0
53            50.0          Shipping            121.0       1500.0          198       Donald 1999-06-21    SH_CLERK    2600             124.0
54            50.0          Shipping            121.0       1500.0          199      Douglas 2000-01-13    SH_CLERK    2600             124.0
55            60.0                IT            103.0       1400.0          103    Alexander 1990-01-03     IT_PROG    9000             102.0
56            60.0                IT            103.0       1400.0          104        Bruce 1991-05-21     IT_PROG    6000             103.0
57            60.0                IT            103.0       1400.0          105        David 1997-06-25     IT_PROG    4800             103.0
58            60.0                IT            103.0       1400.0          106        Valli 1998-02-05     IT_PROG    4800             103.0
59            60.0                IT            103.0       1400.0          107        Diana 1999-02-07     IT_PROG    4200             103.0
60            70.0  Public Relations            204.0       2700.0          204      Hermann 1994-06-07      PR_REP   10000             101.0
61            80.0             Sales            145.0       2500.0          145         John 1996-10-01      SA_MAN   14000             100.0
62            80.0             Sales            145.0       2500.0          146        Karen 1997-01-05      SA_MAN   13500             100.0
63            80.0             Sales            145.0       2500.0          147      Alberto 1997-03-10      SA_MAN   12000             100.0
64            80.0             Sales            145.0       2500.0          148       Gerald 1999-10-15      SA_MAN   11000             100.0
65            80.0             Sales            145.0       2500.0          149        Eleni 2000-01-29      SA_MAN   10500             100.0
66            80.0             Sales            145.0       2500.0          150        Peter 1997-01-30      SA_REP   10000             145.0
67            80.0             Sales            145.0       2500.0          151        David 1997-03-24      SA_REP    9500             145.0
68            80.0             Sales            145.0       2500.0          152        Peter 1997-08-20      SA_REP    9000             145.0
69            80.0             Sales            145.0       2500.0          153  Christopher 1998-03-30      SA_REP    8000             145.0
70            80.0             Sales            145.0       2500.0          154      Nanette 1998-12-09      SA_REP    7500             145.0
71            80.0             Sales            145.0       2500.0          155       Oliver 1999-11-23      SA_REP    7000             145.0
72            80.0             Sales            145.0       2500.0          156      Janette 1996-01-30      SA_REP   10000             146.0
73            80.0             Sales            145.0       2500.0          157      Patrick 1996-03-04      SA_REP    9500             146.0
74            80.0             Sales            145.0       2500.0          158        Allan 1996-08-01      SA_REP    9000             146.0
75            80.0             Sales            145.0       2500.0          159      Lindsey 1997-03-10      SA_REP    8000             146.0
76            80.0             Sales            145.0       2500.0          160       Louise 1997-12-15      SA_REP    7500             146.0
77            80.0             Sales            145.0       2500.0          161       Sarath 1998-11-03      SA_REP    7000             146.0
78            80.0             Sales            145.0       2500.0          162        Clara 1997-11-11      SA_REP   10500             147.0
79            80.0             Sales            145.0       2500.0          163     Danielle 1999-03-19      SA_REP    9500             147.0
80            80.0             Sales            145.0       2500.0          164       Mattea 2000-01-24      SA_REP    7200             147.0
81            80.0             Sales            145.0       2500.0          165        David 2000-02-23      SA_REP    6800             147.0
82            80.0             Sales            145.0       2500.0          166       Sundar 2000-03-24      SA_REP    6400             147.0
83            80.0             Sales            145.0       2500.0          167         Amit 2000-04-21      SA_REP    6200             147.0
84            80.0             Sales            145.0       2500.0          168         Lisa 1997-03-11      SA_REP   11500             148.0
85            80.0             Sales            145.0       2500.0          169     Harrison 1998-03-23      SA_REP   10000             148.0
86            80.0             Sales            145.0       2500.0          170       Tayler 1998-01-24      SA_REP    9600             148.0
87            80.0             Sales            145.0       2500.0          171      William 1999-02-23      SA_REP    7400             148.0
88            80.0             Sales            145.0       2500.0          172    Elizabeth 1999-03-24      SA_REP    7300             148.0
89            80.0             Sales            145.0       2500.0          173      Sundita 2000-04-21      SA_REP    6100             148.0
90            80.0             Sales            145.0       2500.0          174        Ellen 1996-05-11      SA_REP   11000             149.0
91            80.0             Sales            145.0       2500.0          175       Alyssa 1997-03-19      SA_REP    8800             149.0
92            80.0             Sales            145.0       2500.0          176     Jonathon 1998-03-24      SA_REP    8600             149.0
93            80.0             Sales            145.0       2500.0          177         Jack 1998-04-23      SA_REP    8400             149.0
94            80.0             Sales            145.0       2500.0          179      Charles 2000-01-04      SA_REP    6200             149.0
95            90.0         Executive            100.0       1700.0          100       Steven 1987-06-17     AD_PRES   24000               NaN
96            90.0         Executive            100.0       1700.0          101        Neena 1989-09-21       AD_VP   17000             100.0
97            90.0         Executive            100.0       1700.0          102          Lex 1993-01-13       AD_VP   17000             100.0
98            90.0         Executive            100.0       1700.0          301        Smith 1989-06-17     IT_PROG   15000             100.0
99           100.0           Finance            108.0       1700.0          108        Nancy 1994-08-17      FI_MGR   12000             101.0
100          100.0           Finance            108.0       1700.0          109       Daniel 1994-08-16  FI_ACCOUNT    9000             108.0
101          100.0           Finance            108.0       1700.0          110         John 1997-09-28  FI_ACCOUNT    8200             108.0
102          100.0           Finance            108.0       1700.0          111       Ismael 1997-09-30  FI_ACCOUNT    7700             108.0
103          100.0           Finance            108.0       1700.0          112  Jose Manuel 1998-03-07  FI_ACCOUNT    7800             108.0
104          100.0           Finance            108.0       1700.0          113         Luis 1999-12-07  FI_ACCOUNT    6900             108.0
105          110.0        Accounting            205.0       1700.0          205      Shelley 1994-06-07      AC_MGR   12000             101.0
106          110.0        Accounting            205.0       1700.0          206      William 1994-06-07  AC_ACCOUNT    8300             205.0
107          110.0        Accounting            205.0       1700.0          302        _Paul 1993-02-12     IT_PROG   20000             100.0
108          110.0        Accounting            205.0       1700.0          303        Pa%ul 1993-02-12     IT_PROG   20000             100.0
109            NaN               NaN              NaN          NaN          178    Kimberely 1999-05-24      SA_REP    7000             149.0
>>> pd.merge(dpt,emp,on='Department_Id',how='left',suffixes=('_left','_right'))
     Department_Id       Department_Name  Manager_Id_left  Location_Id  Employee_Id         Name  Hire_Date      Job_Id   Salary  Manager_Id_right
0               10        Administration            200.0         1700        200.0     Jennifer 1987-09-17     AD_ASST   4400.0             101.0
1               20             Marketing            201.0         1800        201.0      Michael 1996-02-17      MK_MAN  13000.0             100.0
2               20             Marketing            201.0         1800        202.0          Pat 1997-08-17      MK_REP   6000.0             201.0
3               30            Purchasing            114.0         1700        114.0          Den 1994-12-07      PU_MAN  11000.0             100.0
4               30            Purchasing            114.0         1700        115.0    Alexander 1995-05-18    PU_CLERK   3100.0             114.0
5               30            Purchasing            114.0         1700        116.0       Shelli 1997-12-24    PU_CLERK   2900.0             114.0
6               30            Purchasing            114.0         1700        117.0        Sigal 1997-07-24    PU_CLERK   2800.0             114.0
7               30            Purchasing            114.0         1700        118.0          Guy 1998-11-15    PU_CLERK   2600.0             114.0
8               30            Purchasing            114.0         1700        119.0        Karen 1999-08-10    PU_CLERK   2500.0             114.0
9               40       Human Resources            203.0         2400        203.0        Susan 1994-06-07      HR_REP   6500.0             101.0
10              50              Shipping            121.0         1500        120.0      Matthew 1996-07-18      ST_MAN   8000.0             100.0
11              50              Shipping            121.0         1500        121.0         Adam 1997-04-10      ST_MAN   8200.0             100.0
12              50              Shipping            121.0         1500        122.0        Payam 1995-05-01      ST_MAN   7900.0             100.0
13              50              Shipping            121.0         1500        123.0       Shanta 1997-10-10      ST_MAN   6500.0             100.0
14              50              Shipping            121.0         1500        124.0        Kevin 1999-11-16      ST_MAN   5800.0             100.0
15              50              Shipping            121.0         1500        125.0        Julia 1997-07-16    ST_CLERK   3200.0             120.0
16              50              Shipping            121.0         1500        126.0        Irene 1998-09-28    ST_CLERK   2700.0             120.0
17              50              Shipping            121.0         1500        127.0        James 1999-01-14    ST_CLERK   2400.0             120.0
18              50              Shipping            121.0         1500        128.0       Steven 2000-03-08    ST_CLERK   2200.0             120.0
19              50              Shipping            121.0         1500        129.0        Laura 1997-08-20    ST_CLERK   3300.0             121.0
20              50              Shipping            121.0         1500        130.0        Mozhe 1997-10-30    ST_CLERK   2800.0             121.0
21              50              Shipping            121.0         1500        131.0        James 1997-02-16    ST_CLERK   2500.0             121.0
22              50              Shipping            121.0         1500        132.0           TJ 1999-04-10    ST_CLERK   2100.0             121.0
23              50              Shipping            121.0         1500        133.0        Jason 1996-06-14    ST_CLERK   3300.0             122.0
24              50              Shipping            121.0         1500        134.0      Michael 1998-08-26    ST_CLERK   2900.0             122.0
25              50              Shipping            121.0         1500        135.0           Ki 1999-12-12    ST_CLERK   2400.0             122.0
26              50              Shipping            121.0         1500        136.0        Hazel 2000-02-06    ST_CLERK   2200.0             122.0
27              50              Shipping            121.0         1500        137.0       Renske 1995-07-14    ST_CLERK   3600.0             123.0
28              50              Shipping            121.0         1500        138.0      Stephen 1997-10-26    ST_CLERK   3200.0             123.0
29              50              Shipping            121.0         1500        139.0         John 1998-02-12    ST_CLERK   2700.0             123.0
30              50              Shipping            121.0         1500        140.0       Joshua 1998-04-06    ST_CLERK   2500.0             123.0
31              50              Shipping            121.0         1500        141.0       Trenna 1995-10-17    ST_CLERK   3500.0             124.0
32              50              Shipping            121.0         1500        142.0       Curtis 1997-01-29    ST_CLERK   3100.0             124.0
33              50              Shipping            121.0         1500        143.0      Randall 1998-03-15    ST_CLERK   2600.0             124.0
34              50              Shipping            121.0         1500        144.0        Peter 1998-07-09    ST_CLERK   2500.0             124.0
35              50              Shipping            121.0         1500        180.0      Winston 1998-01-24    SH_CLERK   3200.0             120.0
36              50              Shipping            121.0         1500        181.0         Jean 1998-02-23    SH_CLERK   3100.0             120.0
37              50              Shipping            121.0         1500        182.0       Martha 1999-06-21    SH_CLERK   2500.0             120.0
38              50              Shipping            121.0         1500        183.0       Girard 2000-02-03    SH_CLERK   2800.0             120.0
39              50              Shipping            121.0         1500        184.0      Nandita 1996-01-27    SH_CLERK   4200.0             121.0
40              50              Shipping            121.0         1500        185.0       Alexis 1997-02-20    SH_CLERK   4100.0             121.0
41              50              Shipping            121.0         1500        186.0        Julia 1998-06-24    SH_CLERK   3400.0             121.0
42              50              Shipping            121.0         1500        187.0      Anthony 1999-02-07    SH_CLERK   3000.0             121.0
43              50              Shipping            121.0         1500        188.0        Kelly 1997-06-14    SH_CLERK   3800.0             122.0
44              50              Shipping            121.0         1500        189.0     Jennifer 1997-08-13    SH_CLERK   3600.0             122.0
45              50              Shipping            121.0         1500        190.0      Timothy 1998-07-11    SH_CLERK   2900.0             122.0
46              50              Shipping            121.0         1500        191.0      Randall 1999-12-19    SH_CLERK   2500.0             122.0
47              50              Shipping            121.0         1500        192.0        Sarah 1996-02-04    SH_CLERK   4000.0             123.0
48              50              Shipping            121.0         1500        193.0      Britney 1997-03-03    SH_CLERK   3900.0             123.0
49              50              Shipping            121.0         1500        194.0       Samuel 1998-07-01    SH_CLERK   3200.0             123.0
50              50              Shipping            121.0         1500        195.0        Vance 1999-03-17    SH_CLERK   2800.0             123.0
51              50              Shipping            121.0         1500        196.0        Alana 1998-04-24    SH_CLERK   3100.0             124.0
52              50              Shipping            121.0         1500        197.0        Kevin 1998-05-23    SH_CLERK   3000.0             124.0
53              50              Shipping            121.0         1500        198.0       Donald 1999-06-21    SH_CLERK   2600.0             124.0
54              50              Shipping            121.0         1500        199.0      Douglas 2000-01-13    SH_CLERK   2600.0             124.0
55              60                    IT            103.0         1400        103.0    Alexander 1990-01-03     IT_PROG   9000.0             102.0
56              60                    IT            103.0         1400        104.0        Bruce 1991-05-21     IT_PROG   6000.0             103.0
57              60                    IT            103.0         1400        105.0        David 1997-06-25     IT_PROG   4800.0             103.0
58              60                    IT            103.0         1400        106.0        Valli 1998-02-05     IT_PROG   4800.0             103.0
59              60                    IT            103.0         1400        107.0        Diana 1999-02-07     IT_PROG   4200.0             103.0
60              70      Public Relations            204.0         2700        204.0      Hermann 1994-06-07      PR_REP  10000.0             101.0
61              80                 Sales            145.0         2500        145.0         John 1996-10-01      SA_MAN  14000.0             100.0
62              80                 Sales            145.0         2500        146.0        Karen 1997-01-05      SA_MAN  13500.0             100.0
63              80                 Sales            145.0         2500        147.0      Alberto 1997-03-10      SA_MAN  12000.0             100.0
64              80                 Sales            145.0         2500        148.0       Gerald 1999-10-15      SA_MAN  11000.0             100.0
65              80                 Sales            145.0         2500        149.0        Eleni 2000-01-29      SA_MAN  10500.0             100.0
66              80                 Sales            145.0         2500        150.0        Peter 1997-01-30      SA_REP  10000.0             145.0
67              80                 Sales            145.0         2500        151.0        David 1997-03-24      SA_REP   9500.0             145.0
68              80                 Sales            145.0         2500        152.0        Peter 1997-08-20      SA_REP   9000.0             145.0
69              80                 Sales            145.0         2500        153.0  Christopher 1998-03-30      SA_REP   8000.0             145.0
70              80                 Sales            145.0         2500        154.0      Nanette 1998-12-09      SA_REP   7500.0             145.0
71              80                 Sales            145.0         2500        155.0       Oliver 1999-11-23      SA_REP   7000.0             145.0
72              80                 Sales            145.0         2500        156.0      Janette 1996-01-30      SA_REP  10000.0             146.0
73              80                 Sales            145.0         2500        157.0      Patrick 1996-03-04      SA_REP   9500.0             146.0
74              80                 Sales            145.0         2500        158.0        Allan 1996-08-01      SA_REP   9000.0             146.0
75              80                 Sales            145.0         2500        159.0      Lindsey 1997-03-10      SA_REP   8000.0             146.0
76              80                 Sales            145.0         2500        160.0       Louise 1997-12-15      SA_REP   7500.0             146.0
77              80                 Sales            145.0         2500        161.0       Sarath 1998-11-03      SA_REP   7000.0             146.0
78              80                 Sales            145.0         2500        162.0        Clara 1997-11-11      SA_REP  10500.0             147.0
79              80                 Sales            145.0         2500        163.0     Danielle 1999-03-19      SA_REP   9500.0             147.0
80              80                 Sales            145.0         2500        164.0       Mattea 2000-01-24      SA_REP   7200.0             147.0
81              80                 Sales            145.0         2500        165.0        David 2000-02-23      SA_REP   6800.0             147.0
82              80                 Sales            145.0         2500        166.0       Sundar 2000-03-24      SA_REP   6400.0             147.0
83              80                 Sales            145.0         2500        167.0         Amit 2000-04-21      SA_REP   6200.0             147.0
84              80                 Sales            145.0         2500        168.0         Lisa 1997-03-11      SA_REP  11500.0             148.0
85              80                 Sales            145.0         2500        169.0     Harrison 1998-03-23      SA_REP  10000.0             148.0
86              80                 Sales            145.0         2500        170.0       Tayler 1998-01-24      SA_REP   9600.0             148.0
87              80                 Sales            145.0         2500        171.0      William 1999-02-23      SA_REP   7400.0             148.0
88              80                 Sales            145.0         2500        172.0    Elizabeth 1999-03-24      SA_REP   7300.0             148.0
89              80                 Sales            145.0         2500        173.0      Sundita 2000-04-21      SA_REP   6100.0             148.0
90              80                 Sales            145.0         2500        174.0        Ellen 1996-05-11      SA_REP  11000.0             149.0
91              80                 Sales            145.0         2500        175.0       Alyssa 1997-03-19      SA_REP   8800.0             149.0
92              80                 Sales            145.0         2500        176.0     Jonathon 1998-03-24      SA_REP   8600.0             149.0
93              80                 Sales            145.0         2500        177.0         Jack 1998-04-23      SA_REP   8400.0             149.0
94              80                 Sales            145.0         2500        179.0      Charles 2000-01-04      SA_REP   6200.0             149.0
95              90             Executive            100.0         1700        100.0       Steven 1987-06-17     AD_PRES  24000.0               NaN
96              90             Executive            100.0         1700        101.0        Neena 1989-09-21       AD_VP  17000.0             100.0
97              90             Executive            100.0         1700        102.0          Lex 1993-01-13       AD_VP  17000.0             100.0
98              90             Executive            100.0         1700        301.0        Smith 1989-06-17     IT_PROG  15000.0             100.0
99             100               Finance            108.0         1700        108.0        Nancy 1994-08-17      FI_MGR  12000.0             101.0
100            100               Finance            108.0         1700        109.0       Daniel 1994-08-16  FI_ACCOUNT   9000.0             108.0
101            100               Finance            108.0         1700        110.0         John 1997-09-28  FI_ACCOUNT   8200.0             108.0
102            100               Finance            108.0         1700        111.0       Ismael 1997-09-30  FI_ACCOUNT   7700.0             108.0
103            100               Finance            108.0         1700        112.0  Jose Manuel 1998-03-07  FI_ACCOUNT   7800.0             108.0
104            100               Finance            108.0         1700        113.0         Luis 1999-12-07  FI_ACCOUNT   6900.0             108.0
105            110            Accounting            205.0         1700        205.0      Shelley 1994-06-07      AC_MGR  12000.0             101.0
106            110            Accounting            205.0         1700        206.0      William 1994-06-07  AC_ACCOUNT   8300.0             205.0
107            110            Accounting            205.0         1700        302.0        _Paul 1993-02-12     IT_PROG  20000.0             100.0
108            110            Accounting            205.0         1700        303.0        Pa%ul 1993-02-12     IT_PROG  20000.0             100.0
109            120              Treasury              NaN         1700          NaN          NaN        NaT         NaN      NaN               NaN
110            130         Corporate Tax              NaN         1700          NaN          NaN        NaT         NaN      NaN               NaN
111            140    Control And Credit              NaN         1700          NaN          NaN        NaT         NaN      NaN               NaN
112            150  Shareholder Services              NaN         1700          NaN          NaN        NaT         NaN      NaN               NaN
113            160              Benefits              NaN         1700          NaN          NaN        NaT         NaN      NaN               NaN
114            170         Manufacturing              NaN         1700          NaN          NaN        NaT         NaN      NaN               NaN
115            180          Construction              NaN         1700          NaN          NaN        NaT         NaN      NaN               NaN
116            190           Contracting              NaN         1700          NaN          NaN        NaT         NaN      NaN               NaN
117            200            Operations              NaN         1700          NaN          NaN        NaT         NaN      NaN               NaN
118            210            IT Support              NaN         1700          NaN          NaN        NaT         NaN      NaN               NaN
119            220                   NOC              NaN         1700          NaN          NaN        NaT         NaN      NaN               NaN
120            230           IT Helpdesk              NaN         1700          NaN          NaN        NaT         NaN      NaN               NaN
121            240      Government Sales              NaN         1700          NaN          NaN        NaT         NaN      NaN               NaN
122            250          Retail Sales              NaN         1700          NaN          NaN        NaT         NaN      NaN               NaN
123            260            Recruiting              NaN         1700          NaN          NaN        NaT         NaN      NaN               NaN
124            270               Payroll              NaN         1700          NaN          NaN        NaT         NaN      NaN               NaN
>>> pd.merge(dpt,emp,on='Department_Id',how='inner',suffixes=('_left','_right'))
     Department_Id   Department_Name  Manager_Id_left  Location_Id  Employee_Id         Name  Hire_Date      Job_Id  Salary  Manager_Id_right
0               10    Administration            200.0         1700          200     Jennifer 1987-09-17     AD_ASST    4400             101.0
1               20         Marketing            201.0         1800          201      Michael 1996-02-17      MK_MAN   13000             100.0
2               20         Marketing            201.0         1800          202          Pat 1997-08-17      MK_REP    6000             201.0
3               30        Purchasing            114.0         1700          114          Den 1994-12-07      PU_MAN   11000             100.0
4               30        Purchasing            114.0         1700          115    Alexander 1995-05-18    PU_CLERK    3100             114.0
5               30        Purchasing            114.0         1700          116       Shelli 1997-12-24    PU_CLERK    2900             114.0
6               30        Purchasing            114.0         1700          117        Sigal 1997-07-24    PU_CLERK    2800             114.0
7               30        Purchasing            114.0         1700          118          Guy 1998-11-15    PU_CLERK    2600             114.0
8               30        Purchasing            114.0         1700          119        Karen 1999-08-10    PU_CLERK    2500             114.0
9               40   Human Resources            203.0         2400          203        Susan 1994-06-07      HR_REP    6500             101.0
10              50          Shipping            121.0         1500          120      Matthew 1996-07-18      ST_MAN    8000             100.0
11              50          Shipping            121.0         1500          121         Adam 1997-04-10      ST_MAN    8200             100.0
12              50          Shipping            121.0         1500          122        Payam 1995-05-01      ST_MAN    7900             100.0
13              50          Shipping            121.0         1500          123       Shanta 1997-10-10      ST_MAN    6500             100.0
14              50          Shipping            121.0         1500          124        Kevin 1999-11-16      ST_MAN    5800             100.0
15              50          Shipping            121.0         1500          125        Julia 1997-07-16    ST_CLERK    3200             120.0
16              50          Shipping            121.0         1500          126        Irene 1998-09-28    ST_CLERK    2700             120.0
17              50          Shipping            121.0         1500          127        James 1999-01-14    ST_CLERK    2400             120.0
18              50          Shipping            121.0         1500          128       Steven 2000-03-08    ST_CLERK    2200             120.0
19              50          Shipping            121.0         1500          129        Laura 1997-08-20    ST_CLERK    3300             121.0
20              50          Shipping            121.0         1500          130        Mozhe 1997-10-30    ST_CLERK    2800             121.0
21              50          Shipping            121.0         1500          131        James 1997-02-16    ST_CLERK    2500             121.0
22              50          Shipping            121.0         1500          132           TJ 1999-04-10    ST_CLERK    2100             121.0
23              50          Shipping            121.0         1500          133        Jason 1996-06-14    ST_CLERK    3300             122.0
24              50          Shipping            121.0         1500          134      Michael 1998-08-26    ST_CLERK    2900             122.0
25              50          Shipping            121.0         1500          135           Ki 1999-12-12    ST_CLERK    2400             122.0
26              50          Shipping            121.0         1500          136        Hazel 2000-02-06    ST_CLERK    2200             122.0
27              50          Shipping            121.0         1500          137       Renske 1995-07-14    ST_CLERK    3600             123.0
28              50          Shipping            121.0         1500          138      Stephen 1997-10-26    ST_CLERK    3200             123.0
29              50          Shipping            121.0         1500          139         John 1998-02-12    ST_CLERK    2700             123.0
30              50          Shipping            121.0         1500          140       Joshua 1998-04-06    ST_CLERK    2500             123.0
31              50          Shipping            121.0         1500          141       Trenna 1995-10-17    ST_CLERK    3500             124.0
32              50          Shipping            121.0         1500          142       Curtis 1997-01-29    ST_CLERK    3100             124.0
33              50          Shipping            121.0         1500          143      Randall 1998-03-15    ST_CLERK    2600             124.0
34              50          Shipping            121.0         1500          144        Peter 1998-07-09    ST_CLERK    2500             124.0
35              50          Shipping            121.0         1500          180      Winston 1998-01-24    SH_CLERK    3200             120.0
36              50          Shipping            121.0         1500          181         Jean 1998-02-23    SH_CLERK    3100             120.0
37              50          Shipping            121.0         1500          182       Martha 1999-06-21    SH_CLERK    2500             120.0
38              50          Shipping            121.0         1500          183       Girard 2000-02-03    SH_CLERK    2800             120.0
39              50          Shipping            121.0         1500          184      Nandita 1996-01-27    SH_CLERK    4200             121.0
40              50          Shipping            121.0         1500          185       Alexis 1997-02-20    SH_CLERK    4100             121.0
41              50          Shipping            121.0         1500          186        Julia 1998-06-24    SH_CLERK    3400             121.0
42              50          Shipping            121.0         1500          187      Anthony 1999-02-07    SH_CLERK    3000             121.0
43              50          Shipping            121.0         1500          188        Kelly 1997-06-14    SH_CLERK    3800             122.0
44              50          Shipping            121.0         1500          189     Jennifer 1997-08-13    SH_CLERK    3600             122.0
45              50          Shipping            121.0         1500          190      Timothy 1998-07-11    SH_CLERK    2900             122.0
46              50          Shipping            121.0         1500          191      Randall 1999-12-19    SH_CLERK    2500             122.0
47              50          Shipping            121.0         1500          192        Sarah 1996-02-04    SH_CLERK    4000             123.0
48              50          Shipping            121.0         1500          193      Britney 1997-03-03    SH_CLERK    3900             123.0
49              50          Shipping            121.0         1500          194       Samuel 1998-07-01    SH_CLERK    3200             123.0
50              50          Shipping            121.0         1500          195        Vance 1999-03-17    SH_CLERK    2800             123.0
51              50          Shipping            121.0         1500          196        Alana 1998-04-24    SH_CLERK    3100             124.0
52              50          Shipping            121.0         1500          197        Kevin 1998-05-23    SH_CLERK    3000             124.0
53              50          Shipping            121.0         1500          198       Donald 1999-06-21    SH_CLERK    2600             124.0
54              50          Shipping            121.0         1500          199      Douglas 2000-01-13    SH_CLERK    2600             124.0
55              60                IT            103.0         1400          103    Alexander 1990-01-03     IT_PROG    9000             102.0
56              60                IT            103.0         1400          104        Bruce 1991-05-21     IT_PROG    6000             103.0
57              60                IT            103.0         1400          105        David 1997-06-25     IT_PROG    4800             103.0
58              60                IT            103.0         1400          106        Valli 1998-02-05     IT_PROG    4800             103.0
59              60                IT            103.0         1400          107        Diana 1999-02-07     IT_PROG    4200             103.0
60              70  Public Relations            204.0         2700          204      Hermann 1994-06-07      PR_REP   10000             101.0
61              80             Sales            145.0         2500          145         John 1996-10-01      SA_MAN   14000             100.0
62              80             Sales            145.0         2500          146        Karen 1997-01-05      SA_MAN   13500             100.0
63              80             Sales            145.0         2500          147      Alberto 1997-03-10      SA_MAN   12000             100.0
64              80             Sales            145.0         2500          148       Gerald 1999-10-15      SA_MAN   11000             100.0
65              80             Sales            145.0         2500          149        Eleni 2000-01-29      SA_MAN   10500             100.0
66              80             Sales            145.0         2500          150        Peter 1997-01-30      SA_REP   10000             145.0
67              80             Sales            145.0         2500          151        David 1997-03-24      SA_REP    9500             145.0
68              80             Sales            145.0         2500          152        Peter 1997-08-20      SA_REP    9000             145.0
69              80             Sales            145.0         2500          153  Christopher 1998-03-30      SA_REP    8000             145.0
70              80             Sales            145.0         2500          154      Nanette 1998-12-09      SA_REP    7500             145.0
71              80             Sales            145.0         2500          155       Oliver 1999-11-23      SA_REP    7000             145.0
72              80             Sales            145.0         2500          156      Janette 1996-01-30      SA_REP   10000             146.0
73              80             Sales            145.0         2500          157      Patrick 1996-03-04      SA_REP    9500             146.0
74              80             Sales            145.0         2500          158        Allan 1996-08-01      SA_REP    9000             146.0
75              80             Sales            145.0         2500          159      Lindsey 1997-03-10      SA_REP    8000             146.0
76              80             Sales            145.0         2500          160       Louise 1997-12-15      SA_REP    7500             146.0
77              80             Sales            145.0         2500          161       Sarath 1998-11-03      SA_REP    7000             146.0
78              80             Sales            145.0         2500          162        Clara 1997-11-11      SA_REP   10500             147.0
79              80             Sales            145.0         2500          163     Danielle 1999-03-19      SA_REP    9500             147.0
80              80             Sales            145.0         2500          164       Mattea 2000-01-24      SA_REP    7200             147.0
81              80             Sales            145.0         2500          165        David 2000-02-23      SA_REP    6800             147.0
82              80             Sales            145.0         2500          166       Sundar 2000-03-24      SA_REP    6400             147.0
83              80             Sales            145.0         2500          167         Amit 2000-04-21      SA_REP    6200             147.0
84              80             Sales            145.0         2500          168         Lisa 1997-03-11      SA_REP   11500             148.0
85              80             Sales            145.0         2500          169     Harrison 1998-03-23      SA_REP   10000             148.0
86              80             Sales            145.0         2500          170       Tayler 1998-01-24      SA_REP    9600             148.0
87              80             Sales            145.0         2500          171      William 1999-02-23      SA_REP    7400             148.0
88              80             Sales            145.0         2500          172    Elizabeth 1999-03-24      SA_REP    7300             148.0
89              80             Sales            145.0         2500          173      Sundita 2000-04-21      SA_REP    6100             148.0
90              80             Sales            145.0         2500          174        Ellen 1996-05-11      SA_REP   11000             149.0
91              80             Sales            145.0         2500          175       Alyssa 1997-03-19      SA_REP    8800             149.0
92              80             Sales            145.0         2500          176     Jonathon 1998-03-24      SA_REP    8600             149.0
93              80             Sales            145.0         2500          177         Jack 1998-04-23      SA_REP    8400             149.0
94              80             Sales            145.0         2500          179      Charles 2000-01-04      SA_REP    6200             149.0
95              90         Executive            100.0         1700          100       Steven 1987-06-17     AD_PRES   24000               NaN
96              90         Executive            100.0         1700          101        Neena 1989-09-21       AD_VP   17000             100.0
97              90         Executive            100.0         1700          102          Lex 1993-01-13       AD_VP   17000             100.0
98              90         Executive            100.0         1700          301        Smith 1989-06-17     IT_PROG   15000             100.0
99             100           Finance            108.0         1700          108        Nancy 1994-08-17      FI_MGR   12000             101.0
100            100           Finance            108.0         1700          109       Daniel 1994-08-16  FI_ACCOUNT    9000             108.0
101            100           Finance            108.0         1700          110         John 1997-09-28  FI_ACCOUNT    8200             108.0
102            100           Finance            108.0         1700          111       Ismael 1997-09-30  FI_ACCOUNT    7700             108.0
103            100           Finance            108.0         1700          112  Jose Manuel 1998-03-07  FI_ACCOUNT    7800             108.0
104            100           Finance            108.0         1700          113         Luis 1999-12-07  FI_ACCOUNT    6900             108.0
105            110        Accounting            205.0         1700          205      Shelley 1994-06-07      AC_MGR   12000             101.0
106            110        Accounting            205.0         1700          206      William 1994-06-07  AC_ACCOUNT    8300             205.0
107            110        Accounting            205.0         1700          302        _Paul 1993-02-12     IT_PROG   20000             100.0
108            110        Accounting            205.0         1700          303        Pa%ul 1993-02-12     IT_PROG   20000             100.0
>>> 
>>> 
>>> #Group by operation--------------------------------------
>>> 
>>> emp.columns
Index(['Employee_Id', 'Name', 'Hire_Date', 'Job_Id', 'Salary', 'Manager_Id', 'Department_Id'], dtype='object')
>>> emp.groupby('Department_Id')
<pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001C157499AC8>
>>> 
>>> emp.groupby('Department_Id').aggregate({"Salary":sum})
               Salary
Department_Id        
10.0             4400
20.0            19000
30.0            24900
40.0             6500
50.0           156400
60.0            28800
70.0            10000
80.0           304500
90.0            73000
100.0           51600
110.0           60300
>>> #Above for finding sum of each department salary
>>> 
>>> import numpy as np
>>> emp.groupby('Department_Id').aggregate({"Salary":[sum,max,min]})
               Salary              
                  sum    max    min
Department_Id                      
10.0             4400   4400   4400
20.0            19000  13000   6000
30.0            24900  11000   2500
40.0             6500   6500   6500
50.0           156400   8200   2100
60.0            28800   9000   4200
70.0            10000  10000  10000
80.0           304500  14000   6100
90.0            73000  24000  15000
100.0           51600  12000   6900
110.0           60300  20000   8300
>>> emp.groupby('Department_Id').aggregate({"Salary":[sum,max,min,mean]})
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    emp.groupby('Department_Id').aggregate({"Salary":[sum,max,min,mean]})
NameError: name 'mean' is not defined
>>> emp.groupby('Department_Id').aggregate({"Salary":[sum,max,min,average]})
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    emp.groupby('Department_Id').aggregate({"Salary":[sum,max,min,average]})
NameError: name 'average' is not defined
>>> emp.groupby('Department_Id').aggregate({"Salary":[sum,max,min,np.average]})
               Salary                            
                  sum    max    min       average
Department_Id                                    
10.0             4400   4400   4400   4400.000000
20.0            19000  13000   6000   9500.000000
30.0            24900  11000   2500   4150.000000
40.0             6500   6500   6500   6500.000000
50.0           156400   8200   2100   3475.555556
60.0            28800   9000   4200   5760.000000
70.0            10000  10000  10000  10000.000000
80.0           304500  14000   6100   8955.882353
90.0            73000  24000  15000  18250.000000
100.0           51600  12000   6900   8600.000000
110.0           60300  20000   8300  15075.000000
>>> emp.groupby('Department_Id').aggregate({"Salary":[sum,max,min,np.average]})['Salary']['sum']
Department_Id
10.0       4400
20.0      19000
30.0      24900
40.0       6500
50.0     156400
60.0      28800
70.0      10000
80.0     304500
90.0      73000
100.0     51600
110.0     60300
Name: sum, dtype: int64
>>> emp.groupby('Department_Id').aggregate({"Salary":[sum,max,min,np.average]})['Salary','sum']
Department_Id
10.0       4400
20.0      19000
30.0      24900
40.0       6500
50.0     156400
60.0      28800
70.0      10000
80.0     304500
90.0      73000
100.0     51600
110.0     60300
Name: (Salary, sum), dtype: int64
>>> 
