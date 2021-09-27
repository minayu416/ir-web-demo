# IR Web Demo

There are two languages in this README, please take the elevator of `Table of Contents`

此README有兩個語言版本，可以透過下列`目錄`抵達：


## Table of Contents | 目錄

- [[English Version] IR Web Demo](#en-introduction)
- [[中文介紹] IR Web Demo](#cn-introduction)

<br>

# <span id="en-introduction">IR Web Demo</span>

# Introduction

IR 網站為2016/4進入研究所學習網頁開發的第一個作品，同時也是起初幫忙學校新創立的處室製作的學校網站。

目前學校已無使用此網站，故將先前學校敏感資訊做刪除，使用其他內容填充之，並整理先前的程式碼。

![](https://minayu0416.files.wordpress.com/2019/10/e89ea2e5b995e5bfabe785a7-2019-10-15-e4b88be58d882.00.08.png)

## Development

學習網頁開發前僅修過五堂C語言課程，大學沒有接觸過網頁開發。

這個網頁是代表著本人於網頁開發領域從0開始學習的紀錄，使用語言為簡單的Html, css，參考別的網站的前端，並陸續使用php, python的django架構自行開發後端介面。

- 第一週進度 - 使用 w3schools 學習html, css 並嘗試寫出簡單的一頁前端網頁
- 第二週 - 選取一個網頁前端，搬過來改成自己欲使用的內容(大約耗費兩週)
- 第四週 - 將搬運來的網頁前端改為自己使用的內容(包括圖片, 所有素材自行製作)，自行調整前端排版與動畫以及自己編排內容。
- 第五週 - 將所有頁面使用php改寫(耗費約四周)

- 第九週 - 將所有頁面改用python改寫，使用django架構 (包含學習vim與終端機架設，耗時約六週。)

- 六週後上線使用。

皆為本人於研究所時期半工半讀之時間所開發。

## Features

### Front-end

為 `五個分類靜態展示頁` 以及 `一頁index主頁`，每頁網頁下方可展示十格內容格，由日期遠近排序，由左右按鈕做滑動。縮圖, 日期, 主題與描述皆可調整。

![](https://minayu0416.files.wordpress.com/2019/10/e89ea2e5b995e5bfabe785a7-2019-10-15-e4b88be58d883.12.34.png)

於index主頁有不同的`標籤`代表著不同分類的內容。

包含上方介紹及下方內容可由後台做控制。

![](https://minayu0416.files.wordpress.com/2019/10/e89ea2e5b995e5bfabe785a7-2019-10-15-e4b88be58d883.13.17.png)

若發布內容超過十格也可以使用所有主題，連至其他頁面，並製作新的頁面渲染所有主題。

### Back-end

使用python 之django架構製作網頁後台。使用django內附之陽春主題製作後台。

![](https://minayu0416.files.wordpress.com/2019/10/e89ea2e5b995e5bfabe785a7-2019-10-15-e4b88be58d883.21.48.png)

後台功能如下:

- [前端頁面介紹] 修改, 更新
- [前端內容格] 新增, 刪除, 修改, 更新
- [使用者權限] 新增, 刪除, 修改, 更新 
- [頁面訪問權限] 新增, 刪除, 修改, 更新


#### User permissions

使用者分為 `後台管理者` 與 `內容頁面權限限制`。

`後台管理者` 頁面使用 django 原生提供之權限頁面，superuser由terminal手動創造，其他後台管理者可由superuser登入後台手動新增。

`內容頁面使用者` 則自行開發，介紹如下:


![](https://minayu0416.files.wordpress.com/2019/10/e89ea2e5b995e5bfabe785a7-2019-10-15-e4b88be58d883.22.03.png)

其中 `類別介紹` 與 `文章分類` 頁面需要權限進入。

除後台 `superuser` 為可進入後台頁面之管理者之外，其他使用者欲觀看`類別介紹`, `文章分類` 需透過認證畫面註測權限，並透過LDAP發送認證於先前大學校務系統帳號作認證(現LDAP功能由於Demo先關閉)。

![](https://minayu0416.files.wordpress.com/2019/10/e89ea2e5b995e5bfabe785a7-2019-10-15-e4b88be58d883.37.01.png)

所有註冊與認證紀錄會儲存於 `Users` 與 `Registers`。


# <span id="cn-introduction">IR Web Demo</span>

# 介紹

IR 網站為2016/4進入研究所學習網頁開發的第一個作品，同時也是起初幫忙學校新創立的處室製作的學校網站。

目前學校已無使用此網站，故將先前學校敏感資訊做刪除，使用其他內容填充之，並整理先前的程式碼。

![](https://minayu0416.files.wordpress.com/2019/10/e89ea2e5b995e5bfabe785a7-2019-10-15-e4b88be58d882.00.08.png)

## 開發過程

學習網頁開發前僅修過五堂C語言課程，大學沒有接觸過網頁開發。

這個網頁是代表著本人於網頁開發領域從0開始學習的紀錄，使用語言為簡單的Html, css，參考別的網站的前端，並陸續使用php, python的django架構自行開發後端介面。

- 第一週進度 - 使用 w3schools 學習html, css 並嘗試寫出簡單的一頁前端網頁
- 第二週 - 選取一個網頁前端，搬過來改成自己欲使用的內容(大約耗費兩週)
- 第四週 - 將搬運來的網頁前端改為自己使用的內容(包括圖片, 所有素材自行製作)，自行調整前端排版與動畫以及自己編排內容。
- 第五週 - 將所有頁面使用php改寫(耗費約四周)

- 第九週 - 將所有頁面改用python改寫，使用django架構 (包含學習vim與終端機架設，耗時約六週。)

- 六週後上線使用。

皆為本人於研究所時期半工半讀之時間所開發。

## 開發功能

### 前端功能

為 `五個分類靜態展示頁` 以及 `一頁index主頁`，每頁網頁下方可展示十格內容格，由日期遠近排序，由左右按鈕做滑動。縮圖, 日期, 主題與描述皆可調整。

![](https://minayu0416.files.wordpress.com/2019/10/e89ea2e5b995e5bfabe785a7-2019-10-15-e4b88be58d883.12.34.png)

於index主頁有不同的`標籤`代表著不同分類的內容。

包含上方介紹及下方內容可由後台做控制。

![](https://minayu0416.files.wordpress.com/2019/10/e89ea2e5b995e5bfabe785a7-2019-10-15-e4b88be58d883.13.17.png)

若發布內容超過十格也可以使用所有主題，連至其他頁面，並製作新的頁面渲染所有主題。

### 後端功能

使用python 之django架構製作網頁後台。使用django內附之陽春主題製作後台。

![](https://minayu0416.files.wordpress.com/2019/10/e89ea2e5b995e5bfabe785a7-2019-10-15-e4b88be58d883.21.48.png)

後台功能如下:

- [前端頁面介紹] 修改, 更新
- [前端內容格] 新增, 刪除, 修改, 更新
- [使用者權限] 新增, 刪除, 修改, 更新 
- [頁面訪問權限] 新增, 刪除, 修改, 更新


#### 使用者權限

使用者分為 `後台管理者` 與 `內容頁面權限限制`。

`後台管理者` 頁面使用 django 原生提供之權限頁面，superuser由terminal手動創造，其他後台管理者可由superuser登入後台手動新增。

`內容頁面使用者` 則自行開發，介紹如下:


![](https://minayu0416.files.wordpress.com/2019/10/e89ea2e5b995e5bfabe785a7-2019-10-15-e4b88be58d883.22.03.png)

其中 `類別介紹` 與 `文章分類` 頁面需要權限進入。

除後台 `superuser` 為可進入後台頁面之管理者之外，其他使用者欲觀看`類別介紹`, `文章分類` 需透過認證畫面註測權限，並透過LDAP發送認證於先前大學校務系統帳號作認證(現LDAP功能由於Demo先關閉)。

![](https://minayu0416.files.wordpress.com/2019/10/e89ea2e5b995e5bfabe785a7-2019-10-15-e4b88be58d883.37.01.png)

所有註冊與認證紀錄會儲存於 `Users` 與 `Registers`。



