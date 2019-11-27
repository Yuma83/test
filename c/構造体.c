#include <stdio.h>
#define NUM 5

typedef struct{
	int id;         // 学生番号
	int kokugo;     // 国語の点数
	int sansu;      // 算数の点数
	int rika;          //     理科の点数
	int shakai;     // 社会の点数
	int eigo;       // 英語の点数
}student_data;

void set_data(student_data*,int,int,int,int,int,int);
void get_sum(student_data*);
int sum(student_data*);

int main(void){
	student_data data[NUM];
	int id[] = {1001,1002,1003,1004,1005};
	int kokugo[] = {82,92,43,72,99};
	int sansu[] = {43,83,32,73,72};
	int rika[] = {53,88,53,71,82};
	int shakai[] = {84,79,45,68,91};
	int eigo[] = {45,99,66,59,94};
	
	int sum_array[NUM];
	int tmp;
	
	for (int i = 0; i < NUM; i++){
		set_data(&data[i],id[i],kokugo[i],sansu[i],rika[i],shakai[i],eigo[i]);
		sum_array[i] = sum(&data[i]);
		//printf("%d ",sum_array[i]);
	}
	
	//合計点をソート
	for (int i = 0; i < NUM; i++){
		for (int j = i + 1; j < NUM; j++){
			if(sum_array[i] < sum_array[j]){
				tmp = sum_array[i];
				sum_array[i] = sum_array[j];
				sum_array[j] = tmp;
			}
		}
	}
	//合計点順にソートして出力
	printf("番号\t国語\t数学\t理科\t社会\t英語\t合計\n");
	for (int i = 0; i < NUM; i++){
		for (int j = 0; j < NUM; j++){
			if(sum_array[i] == sum(&data[j])){
				get_sum(&data[j]);
			}
		}
	}
}


// 点数の設定
void set_data(student_data* data,int id,int kokugo,int sansu,int rika,int shakai,int eigo){
	data->id = id;
	data->kokugo = kokugo;
	data->sansu = sansu;
	data->rika = rika;
	data->shakai = shakai;
	data->eigo = eigo;
}

// 個人の点取得
void get_sum(student_data* data)
{
	printf("%d\t",data->id);
	printf("%d\t",data->kokugo);
	printf("%d\t",data->sansu);      // 算数の点数
	printf("%d\t",data->rika);     //     理科の点数
	printf("%d\t",data->shakai);    // 社会の点数
	printf("%d\t",data->eigo);
	printf("%d\t\n",sum(data));
}

//合計点取得
int sum(student_data* data){
	return data->kokugo + data->sansu + data->rika + data->shakai + data->eigo;
}
