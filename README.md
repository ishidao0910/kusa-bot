# Welcome to kusa-bot
このレポジトリでは、github actionsを用いてpushを定期実行します。

# Actions Flow
- 10:00(JST) cronジョブ起動
- pythonの実行環境構築
- pythonファイル(btc_usd.py)実行
- サイトスクレイピング
- 取得した値段をREADME.mdに書き込み保存
- README.mdの編集差分をコミット
- push

<img width="703" alt="スクリーンショット 2022-05-29 13 18 11" src="https://user-images.githubusercontent.com/73809994/170851996-7b6fa57d-9448-48b2-92b5-25197f6f1dce.png">


# Everyday BTC/JPY at 10:00(JST)
<br>2022-05-28 1BTC(JPY): 3691661
<br>2022-05-29 1BTC(JPY): 3672404
<br>2022-05-30 1BTC(JPY): 3812789<br>2022-05-31 1BTC(JPY): 4044251<br>2022-06-01 1BTC(JPY): 4096657<br>2022-06-02 1BTC(JPY): 3864097<br>2022-06-03 1BTC(JPY): 3971973<br>2022-06-04 1BTC(JPY): 3894198<br>2022-06-05 1BTC(JPY): 3887994<br>2022-06-06 1BTC(JPY): 4033669<br>2022-06-07 1BTC(JPY): 3900584<br>2022-06-08 1BTC(JPY): 4146326<br>2022-06-09 1BTC(JPY): 4045510<br>2022-06-10 1BTC(JPY): 4018344<br>2022-06-11 1BTC(JPY): 3922619<br>2022-06-12 1BTC(JPY): 3800348<br>2022-06-13 1BTC(JPY): 3470740<br>2022-06-14 1BTC(JPY): 2836243<br>2022-06-15 1BTC(JPY): 2979207<br>2022-06-16 1BTC(JPY): 3020792<br>2022-06-17 1BTC(JPY): 2785123<br>2022-06-18 1BTC(JPY): 2741033<br>2022-06-19 1BTC(JPY): 2476684<br>2022-06-20 1BTC(JPY): 2766590<br>2022-06-21 1BTC(JPY): 2773068<br>2022-06-22 1BTC(JPY): 2779292<br>2022-06-23 1BTC(JPY): 2767454<br>2022-06-24 1BTC(JPY): 2841564<br>2022-06-25 1BTC(JPY): 2863748<br>2022-06-26 1BTC(JPY): 2891340<br>2022-06-27 1BTC(JPY): 2898676<br>2022-06-28 1BTC(JPY): 2788329<br>2022-06-29 1BTC(JPY): 2768271<br>2022-06-30 1BTC(JPY): 2736045<br>2022-07-01 1BTC(JPY): 2736296<br>2022-07-02 1BTC(JPY): 2596025<br>2022-07-03 1BTC(JPY): 2593255<br>2022-07-04 1BTC(JPY): 2573634<br>2022-07-05 1BTC(JPY): 2758700<br>2022-07-06 1BTC(JPY): 2682476<br>2022-07-07 1BTC(JPY): 2769431<br>2022-07-08 1BTC(JPY): 3004320<br>2022-07-09 1BTC(JPY): 2930676<br>2022-07-10 1BTC(JPY): 2916963<br>2022-07-11 1BTC(JPY): 2812227<br>2022-07-12 1BTC(JPY): 2735144<br>2022-07-13 1BTC(JPY): 2671649<br>2022-07-14 1BTC(JPY): 2798676<br>2022-07-15 1BTC(JPY): 2848392<br>2022-07-16 1BTC(JPY): 2869769<br>2022-07-17 1BTC(JPY): 2933130<br>2022-07-18 1BTC(JPY): 2933130<br>2022-07-19 1BTC(JPY): 3055272<br>2022-07-20 1BTC(JPY): 3211324<br>2022-07-21 1BTC(JPY): 3217485<br>2022-07-22 1BTC(JPY): 3171109<br>2022-07-23 1BTC(JPY): 3106505<br>2022-07-24 1BTC(JPY): 3042565<br>2022-07-25 1BTC(JPY): 2989065<br>2022-07-26 1BTC(JPY): 2873939<br>2022-07-27 1BTC(JPY): 2906334<br>2022-07-28 1BTC(JPY): 3092511<br>2022-07-29 1BTC(JPY): 3197067<br>2022-07-30 1BTC(JPY): 3176457<br>2022-07-31 1BTC(JPY): 3171535<br>2022-08-01 1BTC(JPY): 3102684<br>2022-08-02 1BTC(JPY): 2996860<br>2022-08-03 1BTC(JPY): 3033197<br>2022-08-04 1BTC(JPY): 3102984<br>2022-08-05 1BTC(JPY): 3008193<br>2022-08-06 1BTC(JPY): 3137067<br>2022-08-07 1BTC(JPY): 3101236<br>2022-08-08 1BTC(JPY): 3141859<br>2022-08-09 1BTC(JPY): 3199076<br>2022-08-10 1BTC(JPY): 3091394<br>2022-08-11 1BTC(JPY): 3241529<br>2022-08-12 1BTC(JPY): 3180379<br>2022-08-13 1BTC(JPY): 3265829<br>2022-08-14 1BTC(JPY): 3280072<br>2022-08-15 1BTC(JPY): 3322292<br>2022-08-16 1BTC(JPY): 3195276<br>2022-08-17 1BTC(JPY): 3221888<br>2022-08-18 1BTC(JPY): 3166911<br>2022-08-19 1BTC(JPY): 3116375<br>2022-08-20 1BTC(JPY): 2914435<br>2022-08-21 1BTC(JPY): 2914435<br>2022-08-22 1BTC(JPY): 2958151<br>2022-08-23 1BTC(JPY): 2932145<br>2022-08-24 1BTC(JPY): 2902944<br>2022-08-25 1BTC(JPY): 2946649<br>2022-08-26 1BTC(JPY): 2951629<br>2022-08-27 1BTC(JPY): 2781291<br>2022-08-28 1BTC(JPY): 2768904<br>2022-08-29 1BTC(JPY): 2768904<br>2022-08-30 1BTC(JPY): 2802803<br>2022-08-31 1BTC(JPY): 2818724<br>2022-09-01 1BTC(JPY): 2807664<br>2022-09-02 1BTC(JPY): 2821094<br>2022-09-03 1BTC(JPY): 2791714<br>2022-09-04 1BTC(JPY): 2777058<br>2022-09-05 1BTC(JPY): 2772044<br>2022-09-06 1BTC(JPY): 2779869<br>2022-09-07 1BTC(JPY): 2673371<br>2022-09-08 1BTC(JPY): 2775704<br>2022-09-09 1BTC(JPY): 2788903<br>2022-09-10 1BTC(JPY): 3035121<br>2022-09-11 1BTC(JPY): 3068529<br>2022-09-12 1BTC(JPY): 3110505<br>2022-09-13 1BTC(JPY): 3171455<br>2022-09-14 1BTC(JPY): 2947035<br>2022-09-15 1BTC(JPY): 2876953<br>2022-09-16 1BTC(JPY): 2829832<br>2022-09-17 1BTC(JPY): 2845057<br>2022-09-18 1BTC(JPY): 2868208<br>2022-09-19 1BTC(JPY): 2853137<br>2022-09-20 1BTC(JPY): 2758955<br>2022-09-21 1BTC(JPY): 2758955<br>2022-09-22 1BTC(JPY): 2702959<br>2022-09-23 1BTC(JPY): 2744088<br>2022-09-25 1BTC(JPY): 2771104<br>2022-09-26 1BTC(JPY): 18,797
<br>2022-09-26 1BTC(USD): 18,761<br>2022-09-27 1BTC(USD): 20,200<br>2022-09-28 1BTC(USD): 18,728<br>2022-09-29 1BTC(USD): 19,412<br>2022-09-30 1BTC(USD): 19,368<br>2022-10-01 1BTC(USD): 19,402<br>2022-10-02 1BTC(USD): 19,302<br>2022-10-03 1BTC(USD): 19,139<br>2022-10-04 1BTC(USD): 19,548<br>2022-10-05 1BTC(USD): 20,172<br>2022-10-06 1BTC(USD): 20,317<br>2022-10-07 1BTC(USD): 20,011<br>2022-10-08 1BTC(USD): 19,567<br>2022-10-09 1BTC(USD): 19,377<br>2022-10-10 1BTC(USD): 19,448<br>2022-10-11 1BTC(USD): 19,058<br>2022-10-12 1BTC(USD): 19,069<br>2022-10-13 1BTC(USD): 19,094<br>2022-10-14 1BTC(USD): 19,824<br>2022-10-15 1BTC(USD): 19,197<br>2022-10-16 1BTC(USD): 19,130<br>2022-10-17 1BTC(USD): 19,197<br>2022-10-18 1BTC(USD): 19,535<br>2022-10-19 1BTC(USD): 19,286<br>2022-10-20 1BTC(USD): 19,033<br>2022-10-21 1BTC(USD): 19,109<br>2022-10-22 1BTC(USD): 19,142<br>2022-10-23 1BTC(USD): 19,191<br>2022-10-24 1BTC(USD): 19,385<br>2022-10-25 1BTC(USD): 19,345<br>2022-10-26 1BTC(USD): 20,200<br>2022-10-27 1BTC(USD): 20,683<br>2022-10-28 1BTC(USD): 20,256<br>2022-10-29 1BTC(USD): 20,742<br>2022-10-30 1BTC(USD): 20,776<br>2022-10-31 1BTC(USD): 20,496<br>2022-11-01 1BTC(USD): 20,504<br>2022-11-02 1BTC(USD): 20,507<br>2022-11-03 1BTC(USD): 20,283<br>2022-11-04 1BTC(USD): 20,307<br>2022-11-05 1BTC(USD): 21,371<br>2022-11-06 1BTC(USD): 21,240<br>2022-11-07 1BTC(USD): 20,991<br>2022-11-08 1BTC(USD): 20,513<br>2022-11-09 1BTC(USD): 18,131<br>2022-11-10 1BTC(USD): 16,177<br>2022-11-11 1BTC(USD): 17,151<br>2022-11-12 1BTC(USD): 16,908<br>2022-11-13 1BTC(USD): 16,850<br>2022-11-14 1BTC(USD): 16,030<br>2022-11-15 1BTC(USD): 16,751<br>2022-11-16 1BTC(USD): 16,921<br>2022-11-17 1BTC(USD): 16,664<br>2022-11-18 1BTC(USD): 16,910<br>2022-11-19 1BTC(USD): 16,594<br>2022-11-20 1BTC(USD): 16,674<br>2022-11-21 1BTC(USD): 15,996<br>2022-11-22 1BTC(USD): 15,778<br>2022-11-23 1BTC(USD): 16,461<br>2022-11-24 1BTC(USD): 16,691<br>2022-11-25 1BTC(USD): 16,474<br>2022-11-26 1BTC(USD): 16,635<br>2022-11-27 1BTC(USD): 16,483<br>2022-11-28 1BTC(USD): 16,181<br>2022-11-29 1BTC(USD): 16,274<br>2022-11-30 1BTC(USD): 16,964<br>2022-12-01 1BTC(USD): 17,115<br>2022-12-02 1BTC(USD): 16,870<br>2022-12-03 1BTC(USD): 17,049<br>2022-12-04 1BTC(USD): 16,959<br>2022-12-05 1BTC(USD): 17,273<br>2022-12-06 1BTC(USD): 17,076<br>2022-12-07 1BTC(USD): 17,065<br>2022-12-08 1BTC(USD): 16,814<br>2022-12-09 1BTC(USD): 17,224<br>2022-12-10 1BTC(USD): 17,154<br>2022-12-11 1BTC(USD): 17,150<br>2022-12-12 1BTC(USD): 16,927<br>2022-12-13 1BTC(USD): 17,151<br>2022-12-14 1BTC(USD): 17,753<br>2022-12-15 1BTC(USD): 17,683<br>2022-12-16 1BTC(USD): 17,408<br>2022-12-17 1BTC(USD): 16,668<br>2022-12-18 1BTC(USD): 16,725<br>2022-12-19 1BTC(USD): 16,791<br>2022-12-20 1BTC(USD): 16,566<br>2022-12-21 1BTC(USD): 16,861<br>2022-12-22 1BTC(USD): 16,825<br>2022-12-23 1BTC(USD): 16,785<br>2022-12-24 1BTC(USD): 16,814<br>2022-12-25 1BTC(USD): 16,844<br>2022-12-26 1BTC(USD): 16,870<br>2022-12-27 1BTC(USD): 16,878<br>2022-12-28 1BTC(USD): 16,700<br>2022-12-29 1BTC(USD): 16,517<br>2022-12-30 1BTC(USD): 16,602<br>2022-12-31 1BTC(USD): 16,556<br>2023-01-01 1BTC(USD): 16,537<br>2023-01-02 1BTC(USD): 16,566<br>2023-01-03 1BTC(USD): 16,681<br>2023-01-04 1BTC(USD): 16,716<br>2023-01-05 1BTC(USD): 16,832<br>2023-01-06 1BTC(USD): 16,814<br>2023-01-07 1BTC(USD): 16,945<br>2023-01-08 1BTC(USD): 16,928<br>2023-01-09 1BTC(USD): 17,170