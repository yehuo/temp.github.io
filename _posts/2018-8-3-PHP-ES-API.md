# Client Build
```
require 'vendor/autoload.php';
use Elasticsearch\ClientBuilder;
$client = ClientBuilder::create()->build();
```

# Host Change
```
$hosts = [
    '192.168.1.1:9200',         // IP + Port
    '192.168.1.2',              // Just IP
    'mydomain.server.com:9201', // Domain + Port
    'mydomain2.server.com',     // Just Domain
    'https://localhost',        // SSL to localhost
    'https://192.168.1.3:9200'  // SSL to IP + Port
];
$client = ClientBuilder::create()->setHosts($hosts)->build();    
// No-Chain-Method way
// $clientBuilder = ClientBuilder::create();
// $clientBuilder->setHosts($hosts); 
// $client = $clientBuilder->build(); 
```

# Client Usage
```
$client->index($params);  
$client->get($params);
$client->search($params); //more details than 'get' method
$client->delete($params);
$client->indices()->delete($deleteParams);  //just give an 'index' in '$deleteParams'
$client->indices()->create($params);        //
```

# Description
> Client可以理解为一个RESTful API的终端，所有Core Action都可以在$client对象的方法中找到。Index和cluster的操作则可以在以下两个对象中找到：
- $client->indices()
- $client->cluster()
> 所有Method的使用方法：[Method Index](https://www.elastic.co/guide/en/elasticsearch/client/php-api/current/ElasticsearchPHP_Endpoints.html#Elasticsearch_Clientreindex_reindex)

# Something Else
另外还有专门支持DSL查询的[elasticsearch-php](https://github.com/ongr-io/ElasticsearchDSL)和支持与Laravel应用交互的[laravel-elasticsearch](https://github.com/cviebrock/laravel-elasticsearch).
