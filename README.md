# yan_ocr


```bash
docker build -t yan_ocr:1.0.1 .
docker run -it -v /Users/yan/Downloads/:/yan/ yan_ocr:1.0.1

python test.py
```

<table>
  <thead>
    <tr>
      <th>Input Photo</th>
      <th>Output Tagged Photo</th>
      <th>Output Detected Text</th>
    </tr>
  </thead>
  <tr>
    <td>
      <img src="https://raw.githubusercontent.com/yanliang12/yan_ocr/main/test4.png" height="150">
    </td>
    <td>
      <img src="https://raw.githubusercontent.com/yanliang12/yan_ocr/main/test4_output.png" height="150">
    </td>
    <td>
<pre>
[
  {
    'text': 'LA U R EN', 
    'score': 0.3055954575538635, 
    'coordinate': [[590, 31], 
                  [1021, 31], 
                  [1021, 122], 
                  [590, 122]]
  }, 
  {
    'text': 'RAL PH', 
    'score': 0.24870802462100983, 
    'coordinate': [[177, 35], 
                  [533, 35], 
                  [533, 121], 
                  [177, 121]]
   }
 ]    
</pre>
</td>
</tr>
</table>
