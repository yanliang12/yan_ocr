# yan_ocr


```bash
docker build -t yan_ocr:1.0.1 .
docker run -it -v /Users/yan/Downloads/:/yan/ yan_ocr:1.0.1

python test.py
```

input: 





<table>
  <thead>
    <tr>
      <th>Input activity level data</th>
      <th>Output</th>
    </tr>
  </thead>
  <tr>
    <td>
      <img src="https://raw.githubusercontent.com/yanliang12/yan_ocr/main/test4.png" height="300">
    </td>
    <td>
      <pre>
      <img src="https://raw.githubusercontent.com/yanliang12/yan_ocr/main/test4_output.png" height="300">
{
  'prediction': 'depressed', 
  'confidence': 0.9602384
}
</pre>
    </td>
  </tr>
</table>


output: 

```bash
([[43, 32], [238, 32], [238, 84], [43, 84]], '香梅 路>北', 0.4429141581058502)
([[16, 54], [42, 54], [42, 80], [16, 80]], '南', 0.9915257692337036)
([[60, 75], [149, 75], [149, 99], [60, 99]], 'Xiangmei', 0.5337048172950745)
([[155, 77], [185, 77], [185, 97], [155, 97]], 'Rd', 0.9821609854698181)
```

input: 

![input](/arabic_road_sign.jpg)


output: 

```bash
[[[621, 89], [773, 89], [773, 182], [621, 182]], ' Terminaا [', 0.024632716551423073]
[[[760, 96], [806, 96], [806, 152], [760, 152]], '2', 0.5804283618927002]
[[[666.5430712064641, 202.3775281716354], [739.7070860518412, 196.7070633782251], [741.4569287935359, 225.6224718283646], [667.2929139481588, 231.2929366217749]], 'ديره', 0.760582447052002]
[[[455, 209], [527, 209], [527, 251], [455, 251]], 'جبل', 0.4549483060836792]
[[[373.263428220882, 220.3112561963815], [450.02216633480174, 212.0297848604541], [453.736571779118, 256.68874380361854], [376.97783366519826, 265.97021513954587]], 'علي', 0.4558447003364563]
[[[607, 234], [712, 234], [712, 283], [607, 283]], 'Deira', 0.3672487437725067]
[[[176, 260], [290, 260], [290, 310], [176, 310]], 'ام رمول', 0.17699939012527466]
[[[732.7639320225002, 269.5278640450004], [833.1453606441283, 252.20429165861108], [839.2360679774998, 298.4721359549996], [738.8546393558717, 315.7957083413889]], 'الشار', 0.4488694667816162]
[[[471.5700282971498, 270.94201697828987], [527.4203330701342, 247.81535122350758], [540.4299717028501, 281.05798302171013], [484.57966692986577, 304.1846487764924]], 'ابو', 0.812522828578949]
[[[394.7811992150991, 272.6717988226486], [476.283620807142, 256.7157420472056], [482.2188007849009, 294.3282011773514], [400.716379192858, 309.2842579527944]], 'ظبي', 0.9530214667320251]
[[[701, 273], [747, 273], [747, 309], [701, 309]], 'قة', 0.45831701159477234]
[[[310, 298], [504, 298], [504, 351], [310, 351]], 'Jebel Ati', 0.2335844486951828]
[[[165, 306], [288, 306], [288, 350], [165, 350]], 'الراشدية', 0.6901043057441711]
[[[605, 309], [803, 309], [803, 370], [605, 370]], 'Al Sharjah', 0.21627847850322723]
[[[350, 333], [529, 333], [529, 384], [350, 384]], 'Abu Dhabi', 0.38911423087120056]
[[[48, 347], [282, 347], [282, 398], [48, 398]], '83 Umm Ramool', 0.03810699284076691]
[[[749.2562854188427, 385.5587995863798], [831.7459450972683, 377.79178415720196], [832.7437145811573, 404.4412004136202], [751.2540549027317, 413.20821584279804]], 'مخرج', 0.770193338394165]
[[[83, 387], [259, 387], [259, 431], [83, 431]], 'Al Rashidiya', 0.25348928570747375]
[[[445.1708677174509, 405.6221280326862], [517.7396937478156, 398.7776750971284], [518.829132282549, 423.3778719673138], [447.26030625218436, 430.2223249028716]], 'مخرج', 0.6833480596542358]
[[[752, 410], [820, 410], [820, 440], [752, 440]], 'EXIT', 0.5376325845718384]
[[[454, 423], [519, 423], [519, 455], [454, 455]], 'EXIT', 0.7149630188941956]
```

https://github.com/faustomorales/keras-ocr
