#include <iostream>
#include <math.h>
//#include <windows.h>

// Freeglut library
#include <GL/freeglut.h>

//#define PI_ 3.1416

#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <GL/glut.h>

// Numero PI
#define myPI 3.14159265

// Dom�nio e Contra-Dominio Carteziano para o Exercicio de Tranforma��es
#define MAIORX  400.0f
#define MENORX  00.0f
#define MAIORY  400.0f
#define MENORY  00.0f

GLfloat xmouse, ymouse;

// Dom�nio e Contra-Dominio Carteziano para o Exercicio de Curvas e Superficies
#define MAIORX_BEZIER  400.0f
#define MENORX_BEZIER  0.0f
#define MAIORY_BEZIER  400.0f
#define MENORY_BEZIER  0.0f

// largua e altura das dimen��es da Janela do Windows
#define LARGURA_WINDOW 400
#define ALTURA_WINDOW  400

// posi��o inicial (canto esquerdo superior) da janela Windoes 
#define POSWX 250
#define POSWY 150

// tangentes iniciais e finais dos dois pontos da curva de Hermite
#define tang1x 1000.0f//1000.0f
#define tang1y 0.0f
#define tang2x 1000.0f//-1000.0f
#define tang2y 0.0f

// Polinomio de Bezier e Hermite
GLfloat B[4][2]; // para Bezier
GLfloat P[2][4]; // para Hermite

// variaveis de controle
GLboolean GET_POINTS = 0;   // GET_POINTS = 0 n�o est� pegando pontos; GET_POINTS = 1, est� pegando pontos
GLint     TOTAL_POINTS = 0;  // total de pontos das curvas de Bezier e Hermite

GLfloat bx, by;  // pontos inseridos para as curvas

class Point {
public:
	float x, y;
	void setxAndy(float x2, float y2)
	{
		x = x2; y = y2;
	}
	const Point& operator=(const Point& rPoint)
	{
		x = rPoint.x;
		y = rPoint.y;
		return *this;
	}

};

Point abc[20];
// estrutura para um ponto no espa�o 3D
struct Ponto
{
	GLfloat x;
	GLfloat y;
	GLfloat z;
};


void Inicializa(void);   // fun��o de inicializa��o
void AlteraTamanhoJanela(GLsizei w, GLsizei h);  // fun��o calback de ajuste da janela de visualiza��o
void Teclado(unsigned char key, int x, int y);   // fun��o callback de teclado
void Desenha(void);   // func��o callback principal de desenho (chama todas asa outras)
void myMousefunc(int button, int state, int x, int y);  // fun��o callback de mouse para o exercicio de Tranforma��es
void myMousefuncBezierIterate(int button, int state, int x, int y);   //fun��o callback de mouse para a curva de bezier


GLfloat multiplyHermite(GLfloat T[], GLfloat H[][4], GLfloat M[]);  // fun��o que multiplica as matrizes de hermite
void DesenhaParabola();  // desenha uma parabola simples
void DesenhaHermiteGrau3();  // desenha uma curva de hermite de grau3
void DesenhaBezierGrau3_v3();
void DesenhaEixos();

Ponto P1, P2, P3, P4;


int main(int argc, char** argv)
{
	glutInit(&argc, argv);

	// Define do modo de opera��o da GLUT
	// GLUT_SINGLE significa que vai usar 1 buffer s� (se for usar anima��o ou 3D use GLUT_DOUBLE)
	// aqui, como o c�digo � 2D usamos 1 buffer
	// GLUT_RGB significa que cada pixel � RGB
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);

	// Especifica a posi��o inicial da janela GLUT
	glutInitWindowPosition(POSWX, POSWY);

	// Especifica o tamanho inicial em pixels da janela GLUT
	glutInitWindowSize(LARGURA_WINDOW, ALTURA_WINDOW);

	// Cria a janela passando como argumento o t�tulo da mesma
	glutCreateWindow("Lista 03");

	// Registra a fun��o callback de redesenho da janela de visualiza��o
	glutDisplayFunc(Desenha);

	// Registra a fun��o callback de redimensionamento da janela de visualiza��o
	glutReshapeFunc(AlteraTamanhoJanela);

	// Registra a fun��o callback para tratamento das teclas ASCII
	glutKeyboardFunc(Teclado);

	// Registra a fun��o callback mouse
	glutMouseFunc(myMousefuncBezierIterate);
	//glutMouseFunc(myMousefunc);

	// Chama a fun��o respons�vel por fazer as inicializa��es 
	Inicializa();

	// Inicia o processamento e aguarda intera��es do usu�rio
	glutMainLoop();

	return 0;
}



// Fun��o callback de redesenho da janela de visualiza��o
void Desenha(void)
{

	// Limpa a janela de visualiza��o com a cor  
	// de fundo definida previamente
	glClear(GL_COLOR_BUFFER_BIT);

	// funcao que desenha eixos cartesianos. 
	// Note que esses eixos s�o apenas uma normaliza��o que vc desenha, n�o � o tamanho da janela windows
	DesenhaEixos();

	// DesenhaParabola();
	//DesenhaBezierGrau3_v3(); // usar
	DesenhaHermiteGrau3(); /// usar


	// Executa os comandos OpenGL 
	glFlush();
	//glutPostRedisplay();
}



// Esta fun��o n�o � CallBack de desenho
//ela � chamada pela callback Desenha apenas para separar a tarefa de desenhar das outras tarefas;
// A tarefa aqui � desenhar os eixos cartesianos
//Importante notar que as dimen��es dos eixos cartezianos nao s�o em pixels, como definido no main em glutInitWindowSize
//A escala desses eixos � definida na fun��o void AlteraTamanhoJanela, nas linhas gluOrtho2D...
//� uma quest�o de organiza��o de codigo
//O programa pode funcionar sem ela
void DesenhaEixos()
{
	// Desenha linhas cruzadas
	glColor3f(0.0, 0.0f, 0.0f);
	glBegin(GL_LINES);
	glVertex2f(MENORX, MENORY);
	glVertex2f(xmouse, ymouse);
	glEnd();

	// Desenha a linha vertical
	glColor3f(0.0, 0.0f, 0.0f);
	glBegin(GL_LINES);
	glVertex2f(0.0f, MENORY);
	glVertex2f(0.0f, MAIORY);
	glEnd();

	/// EIXOS 
	// Desenha a linha horizontal
	glColor3f(0.0, 0.0f, 0.0f);
	glBegin(GL_LINES);
	glVertex2f(MENORX, 0.0f);
	glVertex2f(MAIORX, 0.0f);
	glEnd();

}


int fatorial(int n)
{
	if (n <= 1)
		return(1);
	else
		n = n * fatorial(n - 1);
	return n;
}

float binomial(float n, float k)
{
	float resposta;
	resposta = fatorial(n) / (fatorial(k) * fatorial(n - k));
	return resposta;
}

Point drawBezierGeneralized(Point PT[], double t) {
	Point P;
	P.x = 0; P.y = 0;
	for (int i = 0; i < TOTAL_POINTS; i++)
	{
		P.x = P.x + binomial((float)(TOTAL_POINTS - 1), (float)i) * pow(t, (double)i) * pow((1 - t), (TOTAL_POINTS - 1 - i)) * PT[i].x;
		P.y = P.y + binomial((float)(TOTAL_POINTS - 1), (float)i) * pow(t, (double)i) * pow((1 - t), (TOTAL_POINTS - 1 - i)) * PT[i].y;
	}
	//cout<<P.x<<endl<<P.y;
	//cout<<endl<<endl;
	return P;
}

void draw_pixel(int x, int y) {
	glBegin(GL_POINTS);
	glVertex2i(x, y);
	glEnd();
}


// Essa fun��o desenha a curva de Hermite de Grau 3. A matriz de Hermite j� est� colocada
// no c�digo pra vc, � a vari�vel H. Os e pontos de Hermite s�o fornecidos pela interface 
// clicando com o mouse. 
void DesenhaHermiteGrau3()
{

	// Matriz de Hermite de Grau 3
	GLfloat H[4][4] = { { 2.0f, -2.0f,  1.0f,  1.0f },
	{ -3.0f,  3.0f, -2.0f, -1.0f },
	{ 0.0f,  0.0f,  1.0f,  0.0f },
	{ 1.0f,  0.0f,  0.0f,  0.0f } };


	// se o numero de pontos fornecidos for zero, esse trecho de c�digo inicializa s�
	// o primeito ponto, para indicar que o usu�rio clicou em algum lugar, mas
	// ainda b�o clicou no segundo ponto
	// GET_POINTSD = Status de atribui��o de pontos pelo mouse
	if ((TOTAL_POINTS == 0) && (GET_POINTS))
	{
		P[0][0] = bx;  // guarda coordenada x
		P[0][1] = by;  // guarda coordenada y
		P[0][2] = tang1x;  // tangente x do angulo de incid�ncia de entrada 
		P[0][3] = tang1y;  // tangente y do angulo de incid�ncia de entrada
		TOTAL_POINTS = TOTAL_POINTS + 1;
	}


	// se o total de pontos ainda for menor do que 2 e maior do que zero
	// os pontos s�o guardados, juntamente com os �ngulos e tangentes,
	// que devem ser fornecidos diretamente no c�digo
	if ((TOTAL_POINTS > 0) && (GET_POINTS) && (TOTAL_POINTS < 2))
	{
		// testa se o ponto aqul clicado � diferente do anterior
		if ((P[TOTAL_POINTS - 1][0] != bx) && (P[TOTAL_POINTS - 1][1] != by))
		{
			P[TOTAL_POINTS][0] = bx; // guarda coordenada de netrada x
			P[TOTAL_POINTS][1] = by;  // guarda coordenada de entrada y
			P[TOTAL_POINTS][2] = tang2x;  // tangente x do a�ngulo de incid�ncia de sa�da
			P[TOTAL_POINTS][3] = tang2y;  // tangente y do �ngulo de inci�ncia de sa�da
			TOTAL_POINTS = TOTAL_POINTS + 1;
			if (TOTAL_POINTS > 2)  TOTAL_POINTS = 2;
		}
	}



	// exibe os 2  pontos de controle
	glColor3f(1.0, 0.0f, 0.0f);
	glPointSize(5.0f);
	for (int i = 0; i < TOTAL_POINTS; i++)
	{
		//printf("\n%f %f", B[i][0], B[i][1]);
		glBegin(GL_POINTS);
		glVertex2f(P[i][0], P[i][1]);
		glEnd();
	}


	// agora que vc tem os dois pontos e as duas tangentes, que est�o em P
	// basta s� utilizar a teoria vista nos v�deos para montar o polinomio de Hermote 
	// e plotar a curva. N�o se esque�a de variar a vari�vel t de 0 a 1, indo de
	// 0.1 em 0.1, pelo menos, ou 0.01 em 0.01. 
	if (TOTAL_POINTS == 2)
	{
		double t, x, y;
		int x1, y1, x2, y2;

		x1 = P[0][0];
		y1 = P[0][1];
		x2 = P[1][0];
		y2 = P[1][1];

		draw_pixel(x1, y1);
		draw_pixel(x2, y2);

		double f1, f2, f3, f4;

		for (t = 0.001; t < 1; t += 0.001)
		{
			f1 = (2 * t * t * t - 3 * t * t + 1);
			f2 = (-2 * t * t * t + 3 * t * t);
			f3 = (t * t * t - 2 * t * t + t);
			f4 = (t * t * t - t * t);
			x = f1 * x1 + f2 * x2 + f3 * tang1x + f4 * tang2x;
			y = f1 * y1 + f2 * y2 + f3 * tang1y + f4 * tang2y;
			draw_pixel(x, y);
		}

		// calcule aqui sua curva de hermite
	}

	// com todos os pontos calculados, agora vc plota a curva toda
	// se tiver d�vida como fazer isso, observe o c�digo da Fun��o 
	// DesenhaParabola(), nele vcja como a par�bola foi plotada e
	// fa�a o mesmo para a curva de hermite

}

void drawLine(Point p1, Point p2) {
	glBegin(GL_LINES);
	glVertex2f(p1.x, p1.y);
	glVertex2f(p2.x, p2.y);
	glEnd();
	glFlush();
}



void DesenhaBezierGrau3_v3()
{
	const GLint DIMX = MENORX_BEZIER + MAIORX_BEZIER + 1;
	const GLint DIMY = MENORY_BEZIER + MAIORY_BEZIER + 1;

	// esse trecho de c�digo salva s� o primeiro pontos
	// clicado na interface
   // se o numero de pontos fornecidos for zero
   // GET_POINTSD = Status de atribui��o de pontos pelo mouse
	if ((TOTAL_POINTS == 0) && (GET_POINTS))
	{
		B[0][0] = bx; // coordenada x do primeiro ponto
		B[0][1] = by; // ordenada y do primeiro ponto
		TOTAL_POINTS = TOTAL_POINTS + 1;
	}


	// esse segundo trecho salva os demais pontos clicados 
	// da curva de Bezier
   // se o total de pontos ainda for menor do que 4 e maior do que zero
	if ((TOTAL_POINTS > 0) && (GET_POINTS) && (TOTAL_POINTS < 4))
	{
		// testa se o ponto aqul clicado � diferente do anterior
		if ((B[TOTAL_POINTS - 1][0] != bx) && (B[TOTAL_POINTS - 1][1] != by))
		{
			B[TOTAL_POINTS][0] = bx;
			B[TOTAL_POINTS][1] = by;
			TOTAL_POINTS = TOTAL_POINTS + 1;
			if (TOTAL_POINTS > 4)  TOTAL_POINTS = 4;
		}
	}


	// exibe apenas os 4  pontos de controle
	glColor3f(1.0, 0.0f, 0.0f);
	glPointSize(5.0f);
	//printf("\n\n");
	for (int i = 0; i < TOTAL_POINTS; i++)
	{
		//printf("\n%f %f", B[i][0], B[i][1]);
		glBegin(GL_POINTS);
		glVertex2f(B[i][0], B[i][1]);
		glEnd();
	}


	// nesse trecho de codigo, vc deve calcular todos os pontos (nao de controles)
	// por onde passa a curva de Bezier. Para isso, tem que saber a teoria
	if (TOTAL_POINTS == 4)
	{
		for (int i = 0; i < TOTAL_POINTS; i++)
		{
			abc[i].setxAndy(B[i][0], B[i][1]);
		}

		Point p1 = abc[0];

		for (double t = 0.0; t <= 1.0; t += 0.02)
		{
			Point p2 = drawBezierGeneralized(abc, t);
			drawLine(p1, p2);
			p1 = p2;
		}

		TOTAL_POINTS = 3;
	}
}



void DesenhaParabola()
{

	//y = ax^2 + bx + c
	const GLint DIMX = (-1) * MENORX + MAIORX + 1;
	const GLint DIMY = (-1) * MENORY + MAIORY + 1;

	// valores de coordenadas e ordenadas
	GLfloat X[DIMX];
	GLfloat Y[DIMY];

	// par�metros
	GLfloat n = 2; // grau
	GLfloat passo = 0.2; // discretiza��o
	GLfloat a = 0.03;  // constante de x^2
	GLfloat b = 0; // constante de x
	GLfloat c = -20; // constante isolada
	GLfloat xini, yini, xfin, yfin;
	GLfloat x, y;


	glColor3f(1.0, 0.0f, 0.0f);
	x = -50;
	y = a * pow(x, n) + b * x + c;
	xini = x;
	yini = y;


	// plota o primeiro ponto
	glBegin(GL_POINTS);
	glVertex2f(xini, yini);
	glEnd();


	// plota os demais pontos
	for (x = -50 + passo; x < 50; x = x + passo)
	{
		// aqui calcula cada ponto da par�bola
		y = a * pow(x, 2) + b * x + c;
		xfin = x;
		yfin = y;

		// esse trecho plota cada peda�o da par�bola
		// entre seus pontos
		glBegin(GL_LINE_STRIP);
		glVertex2f(xini, yini);
		glVertex2f(xfin, yfin);
		glEnd();
		xini = xfin;
		yini = yfin;
	}

}



// Fun��o callback chamada quando o tamanho da janela � alterado 
void AlteraTamanhoJanela(GLsizei w, GLsizei h)
{
	//GLsizei largura, altura;
	GLfloat largura, altura;

	// Evita a divisao por zero
	if (h == 0) h = 1;

	// Atualiza as vari�veis
	largura = w;
	altura = h;

	// Especifica as dimens�es da Viewport
	glViewport(0, 0, largura, altura);

	// Inicializa o sistema de coordenadas
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();

	// Estabelece a janela de sele��o (esquerda, direita, inferior, 
	// superior) mantendo a propor��o com a janela de visualiza��o
	if (largura <= altura)
		//gluOrtho2D(MENORX, MAIORX, MENORY*altura / largura, MAIORY*altura / largura);
		gluOrtho2D(MENORX_BEZIER, MAIORX_BEZIER, MENORY_BEZIER * altura / largura, MAIORY_BEZIER * altura / largura);
	else
		//gluOrtho2D(MENORX*largura / altura, MAIORX*largura / altura, MENORY, MAIORY);
		gluOrtho2D(MENORX_BEZIER * largura / altura, MAIORX_BEZIER * largura / altura, MENORY_BEZIER, MAIORY_BEZIER);
}


// Fun��o callback chamada para gerenciar eventos de teclas
void Teclado(unsigned char key, int x, int y)
{
	if (key == 27)  // sai comm ESC
		exit(0);
}


// Fun��o respons�vel por inicializar par�metros e vari�veis
void Inicializa(void)
{
	// Define a cor de fundo da janela de visualiza��o como branca
	glClearColor(1.0f, 1.0f, 1.0f, 1.0f);
}


void myMousefuncBezierIterate(int button, int state, int x, int y)
{
	switch (button) {
	case GLUT_LEFT_BUTTON:
	{
		bx = x;
		by = 400 - y;
		GET_POINTS = 1;
		if (TOTAL_POINTS == 4)
		printf("\n %f %f\n", bx, by);
		break;
	}
	case GLUT_RIGHT_BUTTON: {

		GET_POINTS = 0;
		TOTAL_POINTS = 0;
		//glutPostRedisplay();
		break;
	}
	case GLUT_MIDDLE_BUTTON: {

		break;
	}
	};
	glutPostRedisplay();
}




void myMousefunc(int button, int state, int x, int y)
{
	printf("\nmouse na posicao x = %d e y = %d", x, y);

	xmouse = x;
	ymouse = 400 - y;

	switch (button) {
	case GLUT_LEFT_BUTTON:
	{
		printf("\nvoce pressiona o botao esquerdo do mouse");
		break;
	}
	case GLUT_RIGHT_BUTTON: {
		printf("\nvoce pressiona o botao direito do mouse");
		break;
	}
	case GLUT_MIDDLE_BUTTON: {
		printf("\nvoce pressiona o botao do meio do mouse");
		break;
	}
	};

	switch (state) {
	case GLUT_DOWN: {
		printf("\nvoce esta pressionando o botao do mouse");
		break;
	}
	case GLUT_UP: {
		printf("\nvoce soltou o botao do mouse");
		break;
	}
	};

	glutPostRedisplay();

}




// fun��o que multiplica as 3 matrizes de Hermite T * H * M, onde M = {X,Y}
GLfloat multiplyHermite(GLfloat T[], GLfloat H[][4], GLfloat M[])
{

	GLfloat HM[4];

	// m ultiplica primeiro H por M
	for (int i = 0; i < 4; i++)
	{
		HM[i] = 0;
		for (int j = 0; j < 4; j++)
		{
			HM[i] = HM[i] + H[i][j] * M[j];
		}
	}


	// multiplica T * HM
	GLfloat R = 0;
	for (int i = 0; i < 4; i++)
	{
		R = R + T[i] * HM[i];
	}

	return R;
}


/*
GLfloat xponta, yponta;

GLfloat angle, fAspect;

// Largura e altura da janela
GLfloat windowWidth = 400;
GLfloat windowHeight = 400;

// Fun? callback chamada para fazer o desenho
void Desenha(void)
{
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();

	//Limpa a janela de visualiza? com a cor de fundo especificada

	glClear(GL_COLOR_BUFFER_BIT);

	glColor3f(1.0f, 1.0f, 1.0f);
	glBegin(GL_LINES);
	  glVertex2f(0.0,0.0);
	  glVertex2f(xponta,yponta);
	glEnd();

	//Executa os comandos OpenGL
	glFlush();
}

// Inicializa par?tros de rendering
void Inicializa (void)
{
	// Define a cor de fundo da janela de visualiza? como preta
	glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
}


void GerenciaMouse(int button, int state, int x, int y)
{
	xponta = (GLfloat) (x);
	yponta = (GLfloat) (400-y);
	printf("(x,y) = (%d,%d)\n",x,y);
	glutPostRedisplay();
}


// Fun? callback chamada quando o tamanho da janela ?lterado
void AlteraTamanhoJanela(GLsizei w, GLsizei h)
{
				   // Evita a divisao por zero
				   if(h == 0) h = 1;

				   // Especifica as dimens�es da Viewport
				   glViewport(0, 0, w, h);

				   // Inicializa o sistema de coordenadas
				   glMatrixMode(GL_PROJECTION);
				   glLoadIdentity();

				   // Estabelece a janela de sele? (left, right, bottom, top)
				   if (w <= h)
						   gluOrtho2D (0.0f, 400.0f, 0.0f, 400.0f*h/w);
				   else
						   gluOrtho2D (0.0f, 400.0f*w/h, 0.0f, 400.0f);
}


// Programa Principal
int main(int argc, char** argv)
{
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
	glutInitWindowSize(windowWidth,windowHeight);
	glutCreateWindow("Primeiro Programa");
	glutDisplayFunc(Desenha);
	glutMouseFunc(GerenciaMouse);
	glutReshapeFunc(AlteraTamanhoJanela);
	Inicializa();
	glutMainLoop();
}
*/





