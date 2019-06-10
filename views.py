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
	    return render(request, 'index.html',context)
class Get_new_List(APIView):
    def get(self, request):
        activate = Activate.objects.all()
        serialized = activateSerializer(activate, many=True)
        serialized_data=serialized.data[0:3]
        #df = pd.DataFrame.from_dict(serialized_data, orient='columns',index='id')
        #serialized_data=json.loads(serialized_data)
        #df=pd.DataFrame(serialized_data)
        return Response(serialized_data)

def click(request):
	activate=Activate.objects.all()
	serialized=activateSerializer(activate,many=True)
	df=serialized.data[0:10]
	#df=pd.DataFrame(df)
	#df['age']=pd.to_numeric(df['age'])
	#df=df[df['age']>29]
	#
	#df=df.to_json(orient = "records")
	#print (df)
	#context={
	#'df':df
	#}
	#print(context)
	return HttpResponse(df)

class Graph(TemplateView):
	template_name = 'info/second.html'

	def get_context_data(self, *args, **kwargs):
		#context = super(Graph, self).get_context_data(*args,**kwargs)
		#csp_monthwise=pd.read_sql('select * from csp_active_monthwise ',cnx)
		#csp_monthwise['ref_time'] = pd.to_datetime(csp_monthwise['ref_time'])
		#csp_monthwise = csp_monthwise.sort_values(by='ref_time').drop_duplicates(subset=['ref_time'], keep='first')
		#csp_monthwise['ref_time'] = csp_monthwise['ref_time'].dt.to_period('M').astype(str)
		activate = Activate.objects.all()
		serialized = activateSerializer(activate, many=True)
		serialized_data=serialized.data[0:10]
		df=pd.DataFrame(serialized_data)

		
		trace0 = go.Scatter(
    		x=df['age'].values,
    		#y=csp_monthwise['no_of_active_csp'].values,name='Active CSP')
    		y=df['total_monthly_bill'].values)
		#labels = [x for x in csp_monthwise.ref_time]
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
