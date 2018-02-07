#include <bits/stdc++.h>
using namespace std;
int main ()
{
	int n,m,i,j,x,y;
	scanf ("%d%d",&n,&m);
	int a[n+5][m+5];
	pair <int,int> start;
	pair <int,int> end;
	string str;
	for (i = 1; i <= n; i++)
	{
		cin >> str;
		for (j = 0; j < m; j++)
		{
			if (str[j] == 'V')
				start = make_pair (i,j+1);
			else if (str[j] == 'H')
				end = make_pair (i,j+1);
			else if (str[j] == '.')
				a[i][j+1] = 1;
			else
				a[i][j+1] = 0;
		}
	}
	if (start.first > end.second)
		swap (start.first ,end.second);
	int visited[n+5][m+5],go;
	memset (visited,0,sizeof(visited));
	queue <int> que;
	q.push(start.first);
	visited[start.first][start.second] = 1;
	while (!q.empty())
	{
		go = q.pop();
		for (i = go; i <= m; i++)
		{	
			
		}
	}
}


