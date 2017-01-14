100_count,101_count,102_count

	Intersection_id:路口id

	AM_count:早上時段事故count

	PM_count:晚上時段事故count

relation.txt
	
	Intersection_id:路口id

	Rd1_id:路1_id

	Rd2_id:路2_id

	E:東邊路口id

	W

	S

	N


road.txt

	Rd_id:路id

	Rd_name:路名

	spd:路的速度


info.txt
(針對每個案件(CASE_NO)對應到哪個路口(Rd_id),當時路口的四條路(Rd1_1,Rd1_2,Rd2_1,Rd2_2)的狀況(Big,Small,Scooter,PCU,Trun))
		|Rd2_2|
		|	  |
-------        --------
Rd1_1 			  Rd1_2    (Rd1)
-------		   --------
		|     |
		|Rd2_1|

		  Rd2

跟東西南北無關

	CASE_NO:案件編號

	IEOK_01:發生時間 

	ACCD_TP:事故類別(A1、A2、A3) 

	Year:年度 

	x_coord:X座標(TWD67座標)	(事故的X座標)

	y_coord:Y座標(TWD67座標)	(事故的Y座標)

	Rd_id:路口id				(事故對應的路口)

	Latitude:緯度			(事故對應的路口的緯度)

	Longitude:經度			(事故對應的路口的經度)

	Rd1_sp:Rd1速度			

	Rd2_sp:Rd2速度

	Rd1_1_lane:Rd1_1車道數

	Rd1_2_lane:Rd1_2車道數

	Rd2_1_lane:Rd2_1車道數

	Rd2_2_lane:Rd2_2車道數

	lane_id:(RD1_1RD1_2RD2_1RD2_2) (just for me)

	year:資料年份 (just for me)

	Big1_1:大車比例

	Small1_1:小車比例

	Scooter1_1:機車比例

	PCU1_1:PCU

	Trun1_1:轉向比例

	Big1_2:

	Small1_2:

	Scooter1_2:

	PCU1_2:

	Trun1_2:

	Big2_1:

	Small2_1:

	Scooter2_1:

	PCU2_1:

	Trun2_1:

	Big2_2:

	Small2_2:

	Scooter2_2:

	PCU2_2:

	Trun2_2:


	PS:

		Rd1 分成 Rd1_1,Rd1_2(東西向)

		Rd2 分成 Rd2_1,Rd2_2(南北向)