# MOTOMURA

## できること
- アイテムの追加
- レシピの追加
  - レシピの詳細追加
- 買ったものの追加
- 買ったものとレシピとで合致するものの検索

## 想定の環境
- MariaDB
- Flask
- Ubutu 18.0.4
- NGINX

## DB 構造
SQL：
```
CREATE TABLE item_list( `id` INT NOT NULL AUTO_INCREMENT , `name` TEXT NOT NULL , `genre` INT NOT NULL , PRIMARY KEY (`id`));
```
```
CREATE TABLE bought_list ( `id` INT NOT NULL AUTO_INCREMENT , `item_id` INT NOT NULL , `count` INT NOT NULL , `day` DATE NOT NULL , PRIMARY KEY (`id`), FOREIGN KEY (item_id) REFERENCES item_list(id) ON DELETE CASCADE);
```
```
CREATE TABLE recipe_list( `id` INT NOT NULL AUTO_INCREMENT , `name` TEXT NOT NULL , `genre1` INT NOT NULL , `genre2` INT NOT NULL , PRIMARY KEY (`id`));
```
```
CREATE TABLE recipe_detail_list( `id` INT NOT NULL AUTO_INCREMENT , `recipe_id` INT NOT NULL , `item_id` INT NOT NULL , `count` INT NOT NULL , PRIMARY KEY (`id`) , FOREIGN KEY (recipe_id) REFERENCES recipe_list(id) ON DELETE CASCADE, FOREIGN KEY (item_id) REFERENCES item_list(id) ON DELETE CASCADE);
```

## Routing
- home
  - bought(CRD) & recipe search
  - recipe(CRD)
    - detail(CRD)
  - item(CRD)
  
今回はUPDATE機能を除いて作成した。
理由としては、処理が煩雑になるためと最終的に目指す点が動くことのみに重点をおいているためである。

## 実際の動作
[MOTOMURA](https://reina-raft.xyz/village)
