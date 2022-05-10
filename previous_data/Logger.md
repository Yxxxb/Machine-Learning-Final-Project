#### 1. linux

{"datetime":"Sep 27 17:01:01","host_name":"promethus ","sub_name":"systemd","message":"Started Session 3003 of user root.\",\"tags\":[\"beats_input_codec_plain_applied\"]}","_raw":"{\"input\":{\"type\":\"log\"},\"agent\":{\"version\":\"7.4.0\",\"id\":\"8454f5b7-b6e1-414b-a804-beb6717fc6c4\",\"type\":\"filebeat\",\"hostname\":\"promethus\",\"ephemeral_id\":\"f32f567d-1c8d-4ee8-97fe-e07d094a88dd\"},\"ecs\":{\"version\":\"1.1.0\"},\"log\":{\"offset\":44169,\"file\":{\"path\":\"/var/log/messages\"}},\"host\":{\"name\":\"promethus\"},\"message\":\"Sep 27 17:01:01 promethus systemd: Started Session 3003 of user root.\",\"tags\":[\"beats_input_codec_plain_applied\"]}","datatype":"centos_message"}

https://blog.csdn.net/chengxuyuanyonghu/article/details/56009265

在Linux系统中，日志数据主要包括以下三种类型：【内核及系统日志】【用户日志】【程序日志】

日志文件中的每一行表示一条消息，每个消息均由四个字段的固定格式组成。【时间标签】：消息发出的日期和时间。【主机名】：生成消息的计算机的名称。【子系统名称】：发出消息的应用程序的名称。【消息】：消息的具体内容。

#### 2. mysql

{"input":{"type":"log"},"agent":{"id":"8d32405a-fdcc-40b0-a0d4-45e7c0720c3c","hostname":"zabbix","version":"7.4.0","type":"filebeat","ephemeral_id":"6cdfab43-d515-4dc4-945d-672d9a004319"},"ecs":{"version":"1.1.0"},"log":{"file":{"path":"/var/log/mariadb/mariadb-general.log"},"flags":["multiline"],"offset":422309263},"host":{"name":"zabbix"},"message":"210916  9:03:12\t    10 Query\tselect escalationid,actionid,triggerid,eventid,r_eventid,nextcheck,esc_step,status,itemid,acknowledgeid from escalations where triggerid is not null and nextcheck<=1631754195 order by actionid,triggerid,itemid,escalationid\n\t\t    10 Query\tselect actionid,name,status,eventsource,esc_period,pause_suppressed from actions where actionid=3 order by actionid\n\t\t    10 Query\tselect actionid from operations where recovery=1 and actionid=3\n\t\t    10 Query\tselect eventid,source,object,objectid,clock,value,acknowledged,ns,name,severity from events where eventid in (595987,833098) order by eventid\n\t\t    10 Query\tselect distinct eventid from event_suppress where eventid in (595987,833098)\n\t\t    10 Query\tselect eventid,tag,value from event_tag where eventid in (595987,833098) order by eventid\n\t\t    10 Query\tselect triggerid,description,expression,priority,comments,url,recovery_expression,recovery_mode,value,opdata,event_name from triggers where triggerid in (19061,19402)\n\t\t    10 Query\tselect escalationid,actionid,triggerid,eventid,r_eventid,nextcheck,esc_step,status,itemid,acknowledgeid from escalations where triggerid is null and itemid is not null and nextcheck<=1631754195 order by actionid,triggerid,itemid,escalationid\n\t\t    10 Query\tselect escalationid,actionid,triggerid,eventid,r_eventid,nextcheck,esc_step,status,itemid,acknowledgeid from escalations where triggerid is null and itemid is null and nextcheck<=1631754195 order by actionid,triggerid,itemid,escalationid\n\t\t    16 Query\tbegin\n\t\t    16 Query\tselect a.alertid,a.mediatypeid,a.sendto,a.subject,a.message,a.status,a.retries,e.source,e.object,e.objectid,a.parameters,a.eventid,a.p_eventid from alerts a left join events e on a.eventid=e.eventid where alerttype=0 and a.status=3 order by a.alertid\n\t\t    16 Query\tcommit\n\t\t    21 Query\tbegin\n\t\t    21 Query\tinsert into history (itemid,clock,ns,value) values (46032,1631754192,394395850,99.970207000000002),(41712,1631754192,394795731,71.001734841122314),(29172,1631754192,395341015,1.1483209999999999),(34632,1631754192,401035696,0.26686700000000002),(45732,1631754192,402819412,99.961005),(45852,1631754192,404315020,0),(34392,1631754192,408050718,0.14999999999999999),(45492,1631754192,413347428,99.457948999999999)\n\t\t    21 Query\tinsert into history_uint (itemid,clock,ns,value) values (42072,1631754192,402943176,78),(46572,1631754192,404634833,5934530560),(40332,1631754192,406412497,8455712768),(34932,1631754192,406705157,1292772),(37152,1631754192,407135849,3313500160),(37332,1631754192,416961653,0),(41772,1631754192,421678230,0),(34692,1631754192,423663527,0),(45972,1631754192,424979185,1),(45012,1631754192,583273059,983)\n\t\t    21 Query\tcommit\n\t\t    21 Query\tbegin\n\t\t    21 Query\tcommit\n\t\t    21 Query\tbegin\n\t\t    21 Query\tcommit\n\t\t    21 Query\tselect distinct hg.hostid,g.name from hstgrp g,hosts_groups hg where g.groupid=hg.groupid and hg.hostid in (10084,10400,10401,10403,10409,10437,10489,10508,10511,10532,10554,10555,10556,10558,10560,10563)\n\t\t    21 Query\tselect itemid,name from items where itemid in (29172,34392,34632,34692,34932,37152,37332,40332,41712,41772,42072,45012,45492,45732,45852,45972,46032,46572)\n\t\t    21 Query\tselect i.itemid,a.name from applications a,items_applications i where a.applicationid=i.applicationid and i.itemid in (29172,34392,34632,34692,34932,37152,37332,40332,41712,41772,42072,45012,45492,45732,45852,45972,46032,46572)","tags":["beats_input_codec_plain_applied"]}

错误日志 一般/慢查询日志 二进制日志

https://www.cnblogs.com/f-ck-need-u/p/9001061.html

表格内给的例子可能是查询日志 ？

#### 3. ngnix

{"_raw":"{\"input\":{\"type\":\"log\"},\"agent\":{\"version\":\"7.4.0\",\"type\":\"filebeat\",\"ephemeral_id\":\"a532f69e-e3a3-40fc-865a-efb2c6ca8def\",\"id\":\"99a730fc-4f81-4ee8-bb5e-264179d6fcad\",\"hostname\":\"bigops\"},\"ecs\":{\"version\":\"1.1.0\"},\"log\":{\"offset\":59392,\"file\":{\"path\":\"/opt/bigops/logs/work.access.2021-09-17.log\"}},\"host\":{\"name\":\"bigops\"},\"message\":\"10.8.1.28 - [17/Sep/2021:16:00:13 +0800] 'GET work.pscsoft.com/api/overview/host/virt'0.063 200 144 'http://work.pscsoft.com/' 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36' '-'  '-'\",\"tags\":[\"beats_input_codec_plain_applied\"]}","datatype":"nginx_access"}

https://blog.51cto.com/u_13707680/2116001

#### 4. zabbix

{"_raw":"{\"input\":{\"type\":\"log\"},\"agent\":{\"hostname\":\"zabbix\",\"id\":\"e22d9f77-f4e0-4626-b15f-8db4e15b7fd1\",\"type\":\"filebeat\",\"version\":\"7.4.0\",\"ephemeral_id\":\"c902e9c6-1fbf-488e-b434-64164b02ba3b\"},\"ecs\":{\"version\":\"1.1.0\"},\"log\":{\"offset\":540742,\"file\":{\"path\":\"/tmp/dump/problems-history-syncer-1.ndjson\"}},\"host\":{\"name\":\"zabbix\"},\"message\":\"{\\\"clock\\\":1632723187,\\\"ns\\\":838836053,\\\"value\\\":1,\\\"eventid\\\":988849,\\\"name\\\":\\\"sdb: Disk read/write request responses are too high (read > 20 ms for 15m or write > 20 ms for 15m)\\\",\\\"hosts\\\":[{\\\"host\\\":\\\"192.168.100.195\\\",\\\"name\\\":\\\"dm-uat2\\\"}],\\\"groups\\\":[\\\"devteam\\\"],\\\"tags\\\":[]}\",\"tags\":[\"beats_input_codec_plain_applied\"]}"}

#### 5. mongodb

2021-09-01T02:17:52.120+0000 I STORAGE  [initandlisten] WiredTiger message [1630462672:120885][12:0x7f4f518ddb80], txn-recover: Set global recovery timestamp: 0
2021-09-01T02:17:52.125+0000 I RECOVERY [initandlisten] WiredTiger recoveryTimestamp. Ts: Timestamp(0, 0)
2021-09-01T02:17:52.142+0000 I STORAGE  [initandlisten] Starting to check the table logging settings for existing WiredTiger tables
2021-09-01T02:17:52.144+0000 I CONTROL  [initandlisten] 
2021-09-01T02:17:52.145+0000 I CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
2021-09-01T02:17:52.145+0000 I CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
2021-09-01T02:17:52.145+0000 I CONTROL  [initandlisten] 