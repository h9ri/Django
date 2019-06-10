from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Activate
from .serializers import activateSerializer
from django.template import loader
import pandas as pd
import json
from django.shortcuts import HttpResponse
from matplotlib import pylab
from matplotlib.backends.backend_agg import FigureCanvasAgg
from pylab import *
#import pymysql
#from sqlalchemy import create_engine
from django.http import JsonResponse
from django.views.generic import TemplateView
import plotly.graph_objs as go
import plotly
from plotly.offline import plot
import plotly.graph_objs as go
import plotly.offline as opy


class Get_activate_List(APIView):
    def get(self, request):
        activate = Activate.objects.all()
        serialized = activateSerializer(activate, many=True)
        serialized_data=serialized.data[0:3]
        #df = pd.DataFrame.from_dict(serialized_data, orient='columns',index='id')
        #serialized_data=json.loads(serialized_data)
        df=pd.DataFrame(serialized_data)
        return Response(df)
def homepage(request):
	    activate = Activate.objects.all()
	    serialized = activateSerializer(activate, many=True)
	    df=serialized.data[0:10]
	    context={'df':df
	     }
	    print("cxzf")
	    return render(request, 'index.html',context)
class Get_new_List(APIView):
    def get(self, request):
        activate = Activate.objects.all()
        serialized = activateSerializer(activate, many=True)
        serialized_data=serialized.data[0:3]
        return Response(serialized_data)

def click(request):
	activate=Activate.objects.all()
	serialized=activateSerializer(activate,many=True)
	df=serialized.data[0:10]
	#df=pd.DataFrame(df)
	#df['age']=pd.to_numeric(df['age'])
	#df=df[df['age']>29]
	#df=df.to_json(orient = "records")
	#print (df)
	#context={
	#'df':df
	#}
	#print(context)
	return HttpResponse(df)
def search(request):
	activate=Activate.objects.all()
	print("Xgfdg")
	search_id = request.GET.get('value')
	print (search_id)
	serialized=activateSerializer(activate,many=True)
	df=serialized.data[0:10]
	df=df[df['id']==search_id]
	return HttpResponse(df)


class Graph(TemplateView):
	template_name = 'second.html'

	def get_context_data(self, *args, **kwargs):
		context = super(Graph, self).get_context_data(*args,**kwargs)
		activate = Activate.objects.all()
		serialized = activateSerializer(activate, many=True)
		serialized_data=serialized.data[0:10]
		df=pd.DataFrame(serialized_data)

		
		trace0 = go.Scatter(
    		x=df['age'].values,
    		y=df['total_monthly_bill'].values)
		#labels = [x for x in df.id]
		layout = go.Layout(
    		title='Active CSP Monthwise',
    		xaxis=go.layout.XAxis(
        	#ticktext=labels,
    		),
    		yaxis2= dict(
    	    overlaying='y',
        	side='right',
        	showgrid=False,))
		data = go.Figure([trace0], layout=layout)
		plot_div = opy.plot(data, output_type='div', include_plotlyjs=False,auto_open=False)
		
		context['graph'] = plot_div  ##it creates a object(div)
		return context