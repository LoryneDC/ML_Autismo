# Ejemplos de Uso de la API de Predicción de Autismo

Este documento contiene ejemplos de cómo consumir la API desde diferentes lenguajes de programación.

---

## Python

### Usando requests

```python
import requests

url = "http://localhost:8000/predict"

data = {
    "A1_Score": 1,
    "A2_Score": 0,
    "A3_Score": 1,
    "A4_Score": 0,
    "A5_Score": 1,
    "A6_Score": 0,
    "A7_Score": 1,
    "A8_Score": 0,
    "A9_Score": 1,
    "A10_Score": 1,
    "age": 38,
    "gender": "f",
    "ethnicity": "White-European",
    "jaundice": "no",
    "austim": "no",
    "contry_of_res": "United States",
    "used_app_before": "no",
    "result": 6.35,
    "relation": "Self"
}

response = requests.post(url, json=data)

if response.status_code == 200:
    result = response.json()
    print(f"Predicción: {result['prediction_label']}")
    print(f"Probabilidad: {result['probability']:.2%}")
else:
    print(f"Error: {response.status_code}")
    print(response.json())
```

---

## JavaScript/Node.js

### Usando fetch

```javascript
const url = "http://localhost:8000/predict";

const data = {
    A1_Score: 1,
    A2_Score: 0,
    A3_Score: 1,
    A4_Score: 0,
    A5_Score: 1,
    A6_Score: 0,
    A7_Score: 1,
    A8_Score: 0,
    A9_Score: 1,
    A10_Score: 1,
    age: 38,
    gender: "f",
    ethnicity: "White-European",
    jaundice: "no",
    austim: "no",
    contry_of_res: "United States",
    used_app_before: "no",
    result: 6.35,
    relation: "Self"
};

fetch(url, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify(data)
})
.then(response => response.json())
.then(result => {
    console.log(`Predicción: ${result.prediction_label}`);
    console.log(`Probabilidad: ${(result.probability * 100).toFixed(2)}%`);
})
.catch(error => {
    console.error('Error:', error);
});
```

### Usando axios

```javascript
const axios = require('axios');

const url = "http://localhost:8000/predict";

const data = {
    A1_Score: 1,
    A2_Score: 0,
    A3_Score: 1,
    A4_Score: 0,
    A5_Score: 1,
    A6_Score: 0,
    A7_Score: 1,
    A8_Score: 0,
    A9_Score: 1,
    A10_Score: 1,
    age: 38,
    gender: "f",
    ethnicity: "White-European",
    jaundice: "no",
    austim: "no",
    contry_of_res: "United States",
    used_app_before: "no",
    result: 6.35,
    relation: "Self"
};

axios.post(url, data)
    .then(response => {
        console.log(`Predicción: ${response.data.prediction_label}`);
        console.log(`Probabilidad: ${(response.data.probability * 100).toFixed(2)}%`);
    })
    .catch(error => {
        console.error('Error:', error.response?.data || error.message);
    });
```

---

## cURL

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "A1_Score": 1,
    "A2_Score": 0,
    "A3_Score": 1,
    "A4_Score": 0,
    "A5_Score": 1,
    "A6_Score": 0,
    "A7_Score": 1,
    "A8_Score": 0,
    "A9_Score": 1,
    "A10_Score": 1,
    "age": 38,
    "gender": "f",
    "ethnicity": "White-European",
    "jaundice": "no",
    "austim": "no",
    "contry_of_res": "United States",
    "used_app_before": "no",
    "result": 6.35,
    "relation": "Self"
  }'
```

---

## PHP

```php
<?php
$url = "http://localhost:8000/predict";

$data = array(
    "A1_Score" => 1,
    "A2_Score" => 0,
    "A3_Score" => 1,
    "A4_Score" => 0,
    "A5_Score" => 1,
    "A6_Score" => 0,
    "A7_Score" => 1,
    "A8_Score" => 0,
    "A9_Score" => 1,
    "A10_Score" => 1,
    "age" => 38,
    "gender" => "f",
    "ethnicity" => "White-European",
    "jaundice" => "no",
    "austim" => "no",
    "contry_of_res" => "United States",
    "used_app_before" => "no",
    "result" => 6.35,
    "relation" => "Self"
);

$options = array(
    'http' => array(
        'header'  => "Content-Type: application/json\r\n",
        'method'  => 'POST',
        'content' => json_encode($data)
    )
);

$context  = stream_context_create($options);
$response = file_get_contents($url, false, $context);

if ($response === FALSE) {
    die('Error');
}

$result = json_decode($response, true);
echo "Predicción: " . $result['prediction_label'] . "\n";
echo "Probabilidad: " . ($result['probability'] * 100) . "%\n";
?>
```

---

## Java

```java
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.net.URI;

public class AutismPredictionClient {
    public static void main(String[] args) throws Exception {
        String url = "http://localhost:8000/predict";
        
        String jsonData = """
        {
            "A1_Score": 1,
            "A2_Score": 0,
            "A3_Score": 1,
            "A4_Score": 0,
            "A5_Score": 1,
            "A6_Score": 0,
            "A7_Score": 1,
            "A8_Score": 0,
            "A9_Score": 1,
            "A10_Score": 1,
            "age": 38,
            "gender": "f",
            "ethnicity": "White-European",
            "jaundice": "no",
            "austim": "no",
            "contry_of_res": "United States",
            "used_app_before": "no",
            "result": 6.35,
            "relation": "Self"
        }
        """;
        
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(url))
            .header("Content-Type", "application/json")
            .POST(HttpRequest.BodyPublishers.ofString(jsonData))
            .build();
        
        HttpResponse<String> response = client.send(request, 
            HttpResponse.BodyHandlers.ofString());
        
        System.out.println("Status: " + response.statusCode());
        System.out.println("Response: " + response.body());
    }
}
```

---

## C# / .NET

```csharp
using System;
using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        var url = "http://localhost:8000/predict";
        
        var data = new
        {
            A1_Score = 1,
            A2_Score = 0,
            A3_Score = 1,
            A4_Score = 0,
            A5_Score = 1,
            A6_Score = 0,
            A7_Score = 1,
            A8_Score = 0,
            A9_Score = 1,
            A10_Score = 1,
            age = 38,
            gender = "f",
            ethnicity = "White-European",
            jaundice = "no",
            austim = "no",
            contry_of_res = "United States",
            used_app_before = "no",
            result = 6.35,
            relation = "Self"
        };
        
        using var client = new HttpClient();
        var json = JsonSerializer.Serialize(data);
        var content = new StringContent(json, Encoding.UTF8, "application/json");
        
        var response = await client.PostAsync(url, content);
        var responseString = await response.Content.ReadAsStringAsync();
        
        Console.WriteLine($"Status: {response.StatusCode}");
        Console.WriteLine($"Response: {responseString}");
    }
}
```

---

## Go

```go
package main

import (
    "bytes"
    "encoding/json"
    "fmt"
    "io/ioutil"
    "net/http"
)

type PredictionRequest struct {
    A1Score        int     `json:"A1_Score"`
    A2Score        int     `json:"A2_Score"`
    A3Score        int     `json:"A3_Score"`
    A4Score        int     `json:"A4_Score"`
    A5Score        int     `json:"A5_Score"`
    A6Score        int     `json:"A6_Score"`
    A7Score        int     `json:"A7_Score"`
    A8Score        int     `json:"A8_Score"`
    A9Score        int     `json:"A9_Score"`
    A10Score       int     `json:"A10_Score"`
    Age            int     `json:"age"`
    Gender         string  `json:"gender"`
    Ethnicity      string  `json:"ethnicity"`
    Jaundice       string  `json:"jaundice"`
    Austim         string  `json:"austim"`
    ContryOfRes    string  `json:"contry_of_res"`
    UsedAppBefore  string  `json:"used_app_before"`
    Result         float64 `json:"result"`
    Relation       string  `json:"relation"`
}

type PredictionResponse struct {
    Prediction      int     `json:"prediction"`
    PredictionLabel string  `json:"prediction_label"`
    Probability     float64 `json:"probability"`
}

func main() {
    url := "http://localhost:8000/predict"
    
    data := PredictionRequest{
        A1Score:       1,
        A2Score:       0,
        A3Score:       1,
        A4Score:       0,
        A5Score:       1,
        A6Score:       0,
        A7Score:       1,
        A8Score:       0,
        A9Score:       1,
        A10Score:      1,
        Age:           38,
        Gender:        "f",
        Ethnicity:     "White-European",
        Jaundice:      "no",
        Austim:        "no",
        ContryOfRes:   "United States",
        UsedAppBefore: "no",
        Result:        6.35,
        Relation:      "Self",
    }
    
    jsonData, err := json.Marshal(data)
    if err != nil {
        panic(err)
    }
    
    resp, err := http.Post(url, "application/json", bytes.NewBuffer(jsonData))
    if err != nil {
        panic(err)
    }
    defer resp.Body.Close()
    
    body, _ := ioutil.ReadAll(resp.Body)
    
    var result PredictionResponse
    json.Unmarshal(body, &result)
    
    fmt.Printf("Predicción: %s\n", result.PredictionLabel)
    fmt.Printf("Probabilidad: %.2f%%\n", result.Probability*100)
}
```

---

## Ruby

```ruby
require 'net/http'
require 'json'
require 'uri'

url = URI.parse('http://localhost:8000/predict')

data = {
  A1_Score: 1,
  A2_Score: 0,
  A3_Score: 1,
  A4_Score: 0,
  A5_Score: 1,
  A6_Score: 0,
  A7_Score: 1,
  A8_Score: 0,
  A9_Score: 1,
  A10_Score: 1,
  age: 38,
  gender: 'f',
  ethnicity: 'White-European',
  jaundice: 'no',
  austim: 'no',
  contry_of_res: 'United States',
  used_app_before: 'no',
  result: 6.35,
  relation: 'Self'
}

http = Net::HTTP.new(url.host, url.port)
request = Net::HTTP::Post.new(url.path, { 'Content-Type' => 'application/json' })
request.body = data.to_json

response = http.request(request)
result = JSON.parse(response.body)

puts "Predicción: #{result['prediction_label']}"
puts "Probabilidad: #{(result['probability'] * 100).round(2)}%"
```

---

## Ejemplo HTML + JavaScript (Frontend)

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Predicción de Autismo</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
        }
        .result {
            margin-top: 20px;
            padding: 15px;
            border-radius: 5px;
            font-size: 1.2em;
        }
        .asd {
            background-color: #ffebee;
            color: #c62828;
        }
        .no-asd {
            background-color: #e8f5e9;
            color: #2e7d32;
        }
    </style>
</head>
<body>
    <h1>Predicción de Autismo</h1>
    <button onclick="testPrediction()">Realizar Predicción de Prueba</button>
    <div id="result"></div>

    <script>
        async function testPrediction() {
            const url = "http://localhost:8000/predict";
            
            const data = {
                A1_Score: 1,
                A2_Score: 0,
                A3_Score: 1,
                A4_Score: 0,
                A5_Score: 1,
                A6_Score: 0,
                A7_Score: 1,
                A8_Score: 0,
                A9_Score: 1,
                A10_Score: 1,
                age: 38,
                gender: "f",
                ethnicity: "White-European",
                jaundice: "no",
                austim: "no",
                contry_of_res: "United States",
                used_app_before: "no",
                result: 6.35,
                relation: "Self"
            };

            try {
                const response = await fetch(url, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(data)
                });

                const result = await response.json();
                
                const resultDiv = document.getElementById('result');
                const cssClass = result.prediction === 1 ? 'asd' : 'no-asd';
                
                resultDiv.className = `result ${cssClass}`;
                resultDiv.innerHTML = `
                    <strong>Resultado:</strong> ${result.prediction_label}<br>
                    <strong>Probabilidad:</strong> ${(result.probability * 100).toFixed(2)}%
                `;
            } catch (error) {
                document.getElementById('result').innerHTML = 
                    `<div class="result" style="background-color: #ffebee;">Error: ${error.message}</div>`;
            }
        }
    </script>
</body>
</html>
```

---

## Notas Importantes

1. **CORS**: La API tiene CORS habilitado para permitir peticiones desde diferentes orígenes.

2. **URL**: Cambia `http://localhost:8000` por la URL de tu servidor en producción.

3. **Validación**: Todos los campos son obligatorios. La API retornará un error 422 si faltan campos o los valores no son válidos.

4. **Valores válidos**: Consulta el endpoint `/features/info` para obtener listas de valores válidos para campos categóricos.

5. **Respuesta de error**: En caso de error, la API retornará un código de estado HTTP apropiado (400, 422, 500) con detalles del error en formato JSON.
