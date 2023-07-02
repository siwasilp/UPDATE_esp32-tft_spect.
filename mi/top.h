#include "color.h"
// Meter colour schemes
#ifdef __cplusplus
extern "C" {
#endif

uint8_t temprature_sens_read();

#ifdef __cplusplus
}
#endif

uint8_t temprature_sens_read();

#define RED2RED     0
#define GREEN2GREEN 1
#define BLUE2BLUE   2
#define BLUE2RED    3
#define GREEN2RED   4
#define RED2GREEN   5
#define RAINBOW     6

#define xviolet        10
#define xblue          11
#define xlight_blue    12
#define xgreen         13
#define xyellow_green  14
#define xyellow        15
#define xorange        16
#define xred           17
#define xir            18
#define xClear         19

#include <Adafruit_AS7341.h>

Adafruit_AS7341 as7341;

#include <TFT_eSPI.h>
#include <SPI.h>

TFT_eSPI tft = TFT_eSPI();

int vol = 34;
int d1, d2, d3, d4, d5, d6, d7, d8, d9, d10;
int xd1, xd2, xd3, xd4, xd5, xd6, xd7, xd8, xd9, xd10;
int yd1, yd2, yd3, yd4, yd5, yd6, yd7, yd8, yd9, yd10;
String zd1, zd2, zd3, zd4, zd5, zd6, zd7, zd8, zd9, zd10;
int AVG_d = 0;
int reading = 0;
unsigned long period = 20000;
unsigned long last_time = 0;
int timee = 100;

int vo = 0;
int MA = 0;
float offset = 1.75;

void doSomething0();
void doSomething1();
void doSomething2();
void read_X();
void linearMeter(int val, int x, int y, int w, int h, int g, int n, byte s);
