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
<br>2022-09-26 1BTC(USD): 18,761<br>2022-09-27 1BTC(USD): 20,200<br>2022-09-28 1BTC(USD): 18,728<br>2022-09-29 1BTC(USD): 19,412<br>2022-09-30 1BTC(USD): 19,368<br>2022-10-01 1BTC(USD): 19,402<br>2022-10-02 1BTC(USD): 19,302<br>2022-10-03 1BTC(USD): 19,139<br>2022-10-04 1BTC(USD): 19,548<br>2022-10-05 1BTC(USD): 20,172<br>2022-10-06 1BTC(USD): 20,317<br>2022-10-07 1BTC(USD): 20,011<br>2022-10-08 1BTC(USD): 19,567<br>2022-10-09 1BTC(USD): 19,377<br>2022-10-10 1BTC(USD): 19,448<br>2022-10-11 1BTC(USD): 19,058<br>2022-10-12 1BTC(USD): 19,069<br>2022-10-13 1BTC(USD): 19,094<br>2022-10-14 1BTC(USD): 19,824<br>2022-10-15 1BTC(USD): 19,197<br>2022-10-16 1BTC(USD): 19,130<br>2022-10-17 1BTC(USD): 19,197<br>2022-10-18 1BTC(USD): 19,535<br>2022-10-19 1BTC(USD): 19,286<br>2022-10-20 1BTC(USD): 19,033<br>2022-10-21 1BTC(USD): 19,109<br>2022-10-22 1BTC(USD): 19,142<br>2022-10-23 1BTC(USD): 19,191<br>2022-10-24 1BTC(USD): 19,385<br>2022-10-25 1BTC(USD): 19,345<br>2022-10-26 1BTC(USD): 20,200<br>2022-10-27 1BTC(USD): 20,683<br>2022-10-28 1BTC(USD): 20,256<br>2022-10-29 1BTC(USD): 20,742<br>2022-10-30 1BTC(USD): 20,776<br>2022-10-31 1BTC(USD): 20,496<br>2022-11-01 1BTC(USD): 20,504<br>2022-11-02 1BTC(USD): 20,507<br>2022-11-03 1BTC(USD): 20,283<br>2022-11-04 1BTC(USD): 20,307<br>2022-11-05 1BTC(USD): 21,371<br>2022-11-06 1BTC(USD): 21,240<br>2022-11-07 1BTC(USD): 20,991<br>2022-11-08 1BTC(USD): 20,513<br>2022-11-09 1BTC(USD): 18,131<br>2022-11-10 1BTC(USD): 16,177<br>2022-11-11 1BTC(USD): 17,151<br>2022-11-12 1BTC(USD): 16,908<br>2022-11-13 1BTC(USD): 16,850<br>2022-11-14 1BTC(USD): 16,030<br>2022-11-15 1BTC(USD): 16,751<br>2022-11-16 1BTC(USD): 16,921<br>2022-11-17 1BTC(USD): 16,664<br>2022-11-18 1BTC(USD): 16,910<br>2022-11-19 1BTC(USD): 16,594<br>2022-11-20 1BTC(USD): 16,674<br>2022-11-21 1BTC(USD): 15,996<br>2022-11-22 1BTC(USD): 15,778<br>2022-11-23 1BTC(USD): 16,461<br>2022-11-24 1BTC(USD): 16,691<br>2022-11-25 1BTC(USD): 16,474<br>2022-11-26 1BTC(USD): 16,635<br>2022-11-27 1BTC(USD): 16,483<br>2022-11-28 1BTC(USD): 16,181<br>2022-11-29 1BTC(USD): 16,274<br>2022-11-30 1BTC(USD): 16,964<br>2022-12-01 1BTC(USD): 17,115<br>2022-12-02 1BTC(USD): 16,870<br>2022-12-03 1BTC(USD): 17,049<br>2022-12-04 1BTC(USD): 16,959<br>2022-12-05 1BTC(USD): 17,273<br>2022-12-06 1BTC(USD): 17,076<br>2022-12-07 1BTC(USD): 17,065<br>2022-12-08 1BTC(USD): 16,814<br>2022-12-09 1BTC(USD): 17,224<br>2022-12-10 1BTC(USD): 17,154<br>2022-12-11 1BTC(USD): 17,150<br>2022-12-12 1BTC(USD): 16,927<br>2022-12-13 1BTC(USD): 17,151<br>2022-12-14 1BTC(USD): 17,753<br>2022-12-15 1BTC(USD): 17,683<br>2022-12-16 1BTC(USD): 17,408<br>2022-12-17 1BTC(USD): 16,668<br>2022-12-18 1BTC(USD): 16,725<br>2022-12-19 1BTC(USD): 16,791<br>2022-12-20 1BTC(USD): 16,566<br>2022-12-21 1BTC(USD): 16,861<br>2022-12-22 1BTC(USD): 16,825<br>2022-12-23 1BTC(USD): 16,785<br>2022-12-24 1BTC(USD): 16,814<br>2022-12-25 1BTC(USD): 16,844<br>2022-12-26 1BTC(USD): 16,870<br>2022-12-27 1BTC(USD): 16,878<br>2022-12-28 1BTC(USD): 16,700<br>2022-12-29 1BTC(USD): 16,517<br>2022-12-30 1BTC(USD): 16,602<br>2022-12-31 1BTC(USD): 16,556<br>2023-01-01 1BTC(USD): 16,537<br>2023-01-02 1BTC(USD): 16,566<br>2023-01-03 1BTC(USD): 16,681<br>2023-01-04 1BTC(USD): 16,716<br>2023-01-05 1BTC(USD): 16,832<br>2023-01-06 1BTC(USD): 16,814<br>2023-01-07 1BTC(USD): 16,945<br>2023-01-08 1BTC(USD): 16,928<br>2023-01-09 1BTC(USD): 17,170<br>2023-01-10 1BTC(USD): 17,212<br>2023-01-11 1BTC(USD): 17,437<br>2023-01-12 1BTC(USD): 18,259<br>2023-01-13 1BTC(USD): 18,826<br>2023-01-14 1BTC(USD): 20,911<br>2023-01-15 1BTC(USD): 20,722<br>2023-01-16 1BTC(USD): 21,162<br>2023-01-17 1BTC(USD): 21,044<br>2023-01-18 1BTC(USD): 21,219<br>2023-01-19 1BTC(USD): 20,683<br>2023-01-20 1BTC(USD): 21,102<br>2023-01-21 1BTC(USD): 22,656<br>2023-01-22 1BTC(USD): 22,764<br>2023-01-23 1BTC(USD): 22,727<br>2023-01-24 1BTC(USD): 23,109<br>2023-01-25 1BTC(USD): 22,553<br>2023-01-26 1BTC(USD): 23,210<br>2023-01-27 1BTC(USD): 22,742<br>2023-01-28 1BTC(USD): 23,089<br>2023-01-29 1BTC(USD): 23,121<br>2023-01-30 1BTC(USD): 23,629<br>2023-01-31 1BTC(USD): 22,890<br>2023-02-01 1BTC(USD): 23,087<br>2023-02-02 1BTC(USD): 23,944<br>2023-02-03 1BTC(USD): 23,544<br>2023-02-04 1BTC(USD): 23,380<br>2023-02-05 1BTC(USD): 23,350<br>2023-02-06 1BTC(USD): 23,004<br>2023-02-07 1BTC(USD): 22,823<br>2023-02-08 1BTC(USD): 23,281<br>2023-02-09 1BTC(USD): 22,893<br>2023-02-10 1BTC(USD): 21,899<br>2023-02-11 1BTC(USD): 21,637<br>2023-02-12 1BTC(USD): 21,790<br>2023-02-13 1BTC(USD): 21,723<br>2023-02-14 1BTC(USD): 21,744<br>2023-02-15 1BTC(USD): 22,125<br>2023-02-16 1BTC(USD): 24,641<br>2023-02-17 1BTC(USD): 23,815<br>2023-02-18 1BTC(USD): 24,628<br>2023-02-19 1BTC(USD): 24,703<br>2023-02-20 1BTC(USD): 24,316<br>2023-02-21 1BTC(USD): 24,898<br>2023-02-22 1BTC(USD): 24,044<br>2023-02-23 1BTC(USD): 24,190<br>2023-02-24 1BTC(USD): 23,967<br>2023-02-25 1BTC(USD): 23,156<br>2023-02-26 1BTC(USD): 23,095<br>2023-02-27 1BTC(USD): 23,583<br>2023-02-28 1BTC(USD): 23,447<br>2023-03-01 1BTC(USD): 23,273<br>2023-03-02 1BTC(USD): 23,515<br>2023-03-03 1BTC(USD): 22,360<br>2023-03-04 1BTC(USD): 22,352<br>2023-03-05 1BTC(USD): 22,408<br>2023-03-06 1BTC(USD): 22,327<br>2023-03-07 1BTC(USD): 22,467<br>2023-03-08 1BTC(USD): 22,169<br>2023-03-09 1BTC(USD): 21,737<br>2023-03-10 1BTC(USD): 20,087<br>2023-03-11 1BTC(USD): 20,930<br>2023-03-12 1BTC(USD): 20,542<br>2023-03-13 1BTC(USD): 22,568<br>2023-03-14 1BTC(USD): 24,507<br>2023-03-15 1BTC(USD): 25,032<br>2023-03-16 1BTC(USD): 24,485<br>2023-03-17 1BTC(USD): 25,715<br>2023-03-18 1BTC(USD): 27,359<br>2023-03-19 1BTC(USD): 27,160<br>2023-03-20 1BTC(USD): 27,702<br>2023-03-21 1BTC(USD): 27,967<br>2023-03-22 1BTC(USD): 28,188<br>2023-03-23 1BTC(USD): 27,221<br>2023-03-24 1BTC(USD): 28,333<br>2023-03-25 1BTC(USD): 27,533<br>2023-03-26 1BTC(USD): 27,630<br>2023-03-27 1BTC(USD): 27,855<br>2023-03-28 1BTC(USD): 27,064<br>2023-03-29 1BTC(USD): 27,319<br>2023-03-30 1BTC(USD): 28,407<br>2023-03-31 1BTC(USD): 28,140<br>2023-04-01 1BTC(USD): 28,621<br>2023-04-02 1BTC(USD): 28,397<br>2023-04-03 1BTC(USD): 27,703<br>2023-04-04 1BTC(USD): 27,821<br>2023-04-05 1BTC(USD): 28,603<br>2023-04-06 1BTC(USD): 28,069<br>2023-04-07 1BTC(USD): 28,083<br>2023-04-08 1BTC(USD): 27,924<br>2023-04-09 1BTC(USD): 28,101<br>2023-04-10 1BTC(USD): 28,323<br>2023-04-11 1BTC(USD): 30,214<br>2023-04-12 1BTC(USD): 30,199<br>2023-04-13 1BTC(USD): 30,093<br>2023-04-14 1BTC(USD): 30,823<br>2023-04-15 1BTC(USD): 30,400<br>2023-04-16 1BTC(USD): 30,283<br>2023-04-17 1BTC(USD): 29,965<br>2023-04-18 1BTC(USD): 29,388<br>2023-04-19 1BTC(USD): 30,238<br>2023-04-20 1BTC(USD): 28,944<br>2023-04-21 1BTC(USD): 28,197<br>2023-04-22 1BTC(USD): 27,284<br>2023-04-23 1BTC(USD): 27,553<br>2023-04-24 1BTC(USD): 27,765<br>2023-04-25 1BTC(USD): 27,405<br>2023-04-26 1BTC(USD): 28,399<br>2023-04-27 1BTC(USD): 28,750<br>2023-04-28 1BTC(USD): 29,524<br>2023-04-29 1BTC(USD): 29,296<br>2023-04-30 1BTC(USD): 29,114<br>2023-05-01 1BTC(USD): 28,510<br>2023-05-02 1BTC(USD): 27,947<br>2023-05-03 1BTC(USD): 28,550<br>2023-05-04 1BTC(USD): 29,082<br>2023-05-05 1BTC(USD): 29,325<br>2023-05-06 1BTC(USD): 29,564<br>2023-05-07 1BTC(USD): 28,961<br>2023-05-08 1BTC(USD): 28,270<br>2023-05-09 1BTC(USD): 27,718<br>2023-05-10 1BTC(USD): 27,711<br>2023-05-11 1BTC(USD): 27,577<br>2023-05-12 1BTC(USD): 26,883<br>2023-05-13 1BTC(USD): 26,848<br>2023-05-14 1BTC(USD): 26,751<br>2023-05-15 1BTC(USD): 27,227<br>2023-05-16 1BTC(USD): 27,029<br>2023-05-17 1BTC(USD): 27,174<br>2023-05-18 1BTC(USD): 27,323<br>2023-05-19 1BTC(USD): 26,813<br>2023-05-20 1BTC(USD): 26,872<br>2023-05-21 1BTC(USD): 27,169<br>2023-05-22 1BTC(USD): 26,557<br>2023-05-23 1BTC(USD): 27,000<br>2023-05-24 1BTC(USD): 27,151<br>2023-05-25 1BTC(USD): 26,122<br>2023-05-26 1BTC(USD): 26,418<br>2023-05-27 1BTC(USD): 26,727<br>2023-05-28 1BTC(USD): 27,099<br>2023-05-29 1BTC(USD): 28,175<br>2023-05-30 1BTC(USD): 27,774<br>2023-05-31 1BTC(USD): 27,695<br>2023-06-01 1BTC(USD): 27,039<br>2023-06-02 1BTC(USD): 26,899<br>2023-06-03 1BTC(USD): 27,161<br>2023-06-04 1BTC(USD): 27,058<br>2023-06-05 1BTC(USD): 27,085<br>2023-06-06 1BTC(USD): 25,770<br>2023-06-07 1BTC(USD): 27,022<br>2023-06-08 1BTC(USD): 26,398<br>2023-06-09 1BTC(USD): 26,337<br>2023-06-10 1BTC(USD): 26,397<br>2023-06-11 1BTC(USD): 25,793<br>2023-06-12 1BTC(USD): 25,903<br>2023-06-13 1BTC(USD): 25,955<br>2023-06-14 1BTC(USD): 26,012<br>2023-06-15 1BTC(USD): 25,072<br>2023-06-16 1BTC(USD): 25,489<br>2023-06-17 1BTC(USD): 26,194<br>2023-06-18 1BTC(USD): 26,483<br>2023-06-19 1BTC(USD): 26,450<br>2023-06-20 1BTC(USD): 26,894<br>2023-06-21 1BTC(USD): 28,822<br>2023-06-22 1BTC(USD): 30,126<br>2023-06-23 1BTC(USD): 29,895<br>2023-06-24 1BTC(USD): 30,639<br>2023-06-25 1BTC(USD): 30,682<br>2023-06-26 1BTC(USD): 30,171<br>2023-06-27 1BTC(USD): 30,394<br>2023-06-28 1BTC(USD): 30,508<br>2023-06-29 1BTC(USD): 30,170<br>2023-06-30 1BTC(USD): 30,482<br>2023-07-01 1BTC(USD): 30,489<br>2023-07-02 1BTC(USD): 30,586<br>2023-07-03 1BTC(USD): 30,740<br>2023-07-04 1BTC(USD): 31,273<br>2023-07-05 1BTC(USD): 30,847<br>2023-07-06 1BTC(USD): 30,489<br>2023-07-07 1BTC(USD): 30,089