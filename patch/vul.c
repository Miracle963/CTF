#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

char *note[10];

int read_int(){
	char buf[16];
	if (__read_chk(0,buf,15,15)<=0){
		puts("read error");
		exit(1);
	}
	return (unsigned int)atoi(buf);
}

void add_note(){
	for (int i=0;i<10;++i){
		if(!note[i]){
			printf("size:");
			int size = read_int();
			note[i] = malloc(size); 
			printf("what do you want to write:");
			read(0,note[i],size);
			return;
		}
	}
	puts("Fulls!");
}

void delete_note(){
	printf("index:");
	int idx = read_int();
	if(note[idx]){ 
		free(note[idx]);
		//note[idx] = 0 double free
		return;
	}
	puts("No such note");
}

void show_note(){
	printf("index:");
	int idx = read_int();
	if(note[idx]){
		printf("%s",note[idx]);
		return;
	}
	puts("No this note");
}

void menu(){
	puts("--------------------");
	puts("1.add a note");
	puts("2.delete a note");
	puts("3.show a note");
	puts("4.exit");
	puts("--------------------");
	puts("Your choice:");
}

int main(){
	setvbuf(stdin,0,2,0);
	setvbuf(stdout,0,2,0);
	setvbuf(stderr,0,2,0);
	while(1){
		menu();
		switch( read_int()){
			case 1:
				add_note();
				break;
			case 2:
				delete_note();
				break;
			case 3:
				show_note();
				break;
			case 4:
				printf("Bye!\n");
				_exit(0);
			default:
				puts("Invalid choice!");
				break;
		}
	}
	return 0;
}