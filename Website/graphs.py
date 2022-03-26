#impor librar
from matplotlib.pyplot import title
from numpy import tile
import pandas as pd
from datetime import datetime
import plotly.express as px
from wordcloud import WordCloud

#read data
df=pd.read_csv('youtube_all_district.csv')
# change publish_time to datetime format
df['publish_time'] = df.apply(lambda r: datetime.strptime(r['publish_time'],'%Y-%m-%d %H:%M:%S'), axis=1)

#df_subset for actual use in functions
df_subset = df.copy()

#Const values
ALL_CATEGORY = set(df['category_id'])
ALL_REGION = set(df['region'])
ALL_CHANNEL = set(df['channel_title'])

MAX_REGION_VIDEOS = df.groupby(['region']).size().reset_index(name='counts').max().counts #max number of video
MAX_REGION_VIEWS = (df.groupby(['region'])['views'].sum()/df.groupby(['region']).size()).max() #max number of average views
MAX_REGION_LIKES_RATIO = (df.groupby(['region'])['likes'].sum()/df.groupby(['region']).size()).max() #max number of average likes
MAX_REGION_DISLIKES_RATIO = (df.groupby(['region'])['dislikes'].sum()/df.groupby(['region']).size()).max() #max number of average dislikes
MAX_REGION_COMMENT_COUNT_RATIO = (df.groupby(['region'])['comment_count'].sum()/df.groupby(['region']).size()).max() #max number of average comment_count

MAX_CHANNEL_VIDEOS = df.groupby(['channel_title']).size().reset_index(name='counts').max().counts #max number of video
MAX_CHANNEL_VIEWS = (df.groupby(['channel_title'])['views'].sum()/df.groupby(['channel_title']).size()).max() #max number of average views
MAX_CHANNEL_LIKES_RATIO = (df.groupby(['channel_title'])['likes'].sum()/df.groupby(['channel_title']).size()).max() #max number of average likes
MAX_CHANNEL_DISLIKES_RATIO = (df.groupby(['channel_title'])['dislikes'].sum()/df.groupby(['channel_title']).size()).max() #max number of average dislikes
MAX_CHANNEL_COMMENT_COUNT_RATIO = (df.groupby(['channel_title'])['comment_count'].sum()/df.groupby(['channel_title']).size()).max() #max number of average comment_count

def setDataFilter(time_range=(datetime(2015, 1, 1, 0, 0, 0),datetime(2020, 1, 1, 0, 0, 0)), category=ALL_CATEGORY, region=ALL_REGION, rank_range=(0,1), channel=ALL_CHANNEL):
  df_filtered = df.copy()
  
  #publish time range
  if time_range!=(datetime(2015, 1, 1, 0, 0, 0),datetime(2020, 1, 1, 0, 0, 0)):
    df_filtered = df_filtered[df_filtered.apply(lambda r: r['publish_time']>=time_range[0] and r['publish_time']<=time_range[1], axis=1)]

  #category filter
  if category != ALL_CATEGORY:
    df_filtered = df_filtered[df_filtered['category_id'].isin(category)]

  #region filter
  if region != ALL_REGION:
    df_filtered = df_filtered[df_filtered['region'].isin(region)]

  #channel rank with in range
  if rank_range!=(0,1):
    num_channel = len(set(df_filtered['channel_title']))
    df_filtered = df_filtered[df_filtered['channel_rank'].between(num_channel*rank_range[0],num_channel*rank_range[1])]

  #channel filter
  if channel!=ALL_CHANNEL:
    df_filtered = df_filtered[df_filtered['channel_title'].isin(channel)]

  return df_filtered

def drawWordCloud(df_subset):

    #Data
    def tagsList(tagString):
        try:
            return tagString.replace('"','').split("|")
        except:
            return []

    tag_list = df_subset.apply(lambda r: tagsList(r['tags']), axis=1)
    
    tag_all = [x for y in tag_list for x in y]
    
    #with open('tags.txt', 'w') as f:
    #  for item in tag_all:
    #      f.write("%s\n" % item)

    #WordCloud
    wc = WordCloud(width=1200, height=500, 
                         collocations=False, background_color="white", 
                         colormap="tab20b").generate(" ".join(tag_all))
    return wc.to_image()
    
def drawRadarGraph(df_subset, type='region'):

    #Data
    if type=='region':
        num_video = df_subset.shape[0]
        views_score = df_subset['views'].sum()/num_video/MAX_REGION_VIEWS*5
        likes_score = df_subset['likes'].sum()/num_video/MAX_REGION_LIKES_RATIO*5
        dislikes_score = df_subset['dislikes'].sum()/num_video/MAX_REGION_DISLIKES_RATIO*5
        comment_count_score = df_subset['comment_count'].sum()/num_video/MAX_REGION_COMMENT_COUNT_RATIO*5
        videos_score = num_video/MAX_REGION_VIDEOS*5
    elif type=='channel':
        num_video = df_subset.shape[0]
        views_score = df_subset['views'].sum()/num_video/MAX_CHANNEL_VIEWS*5
        likes_score = df_subset['likes'].sum()/num_video/MAX_CHANNEL_LIKES_RATIO*5
        dislikes_score = df_subset['dislikes'].sum()/num_video/MAX_CHANNEL_DISLIKES_RATIO*5
        comment_count_score = df_subset['comment_count'].sum()/num_video/MAX_CHANNEL_COMMENT_COUNT_RATIO*5
        videos_score = num_video/MAX_CHANNEL_VIDEOS*5



    df_radar = pd.DataFrame(dict(
        r = [views_score, likes_score, dislikes_score, comment_count_score, videos_score],
        theta = ['views_ratio', 'likes_ratio', 'dislikes_ratio', 'comment_count_ratio', 'num_videos']
    ))
    print(df_radar)

    #Plotly
    import plotly.express as px
    fig = px.line_polar(df_radar, r='r', theta='theta', line_close=True)
    fig.update_traces(fill='toself')
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
            visible=True,
            range=[0, 5]
            )),
        showlegend=False
    )
    #fig.show()
    return fig

def drawPublishTimeDistribution(df_subset):
  df_filtered = df_subset.copy()
  print(df_subset.shape)
  print(df_filtered.shape)
  try:
    df_filtered['publish_time_hour'] = df_filtered.apply(lambda r: r['publish_time'].hour, axis=1)
  except:
    df_filtered['publish_time_hour'] = None
  fig = px.histogram(df_filtered, x="publish_time_hour", color="category_id")
  return fig

def drawNumVideoTrend(df_subset):
  df_video_trend = df_subset.groupby(['category_id',pd.Grouper(key='publish_time', axis=0, freq='D')]).count()
  df_video_trend = pd.DataFrame(df_video_trend.to_records())
  fig = px.line(df_video_trend, x='publish_time', y='video_id', color='category_id')
  return fig

def drawViewVideoTrend(df_subset):
  df_video_trend = df_subset.groupby(['category_id',pd.Grouper(key='publish_time', axis=0, freq='D')]).sum()
  df_video_trend = pd.DataFrame(df_video_trend.to_records())
  fig = px.line(df_video_trend, x='publish_time', y='views', color='category_id')
  return fig

def drawLikeVideoTrend(df_subset):
  df_video_trend = df_subset.groupby(['category_id',pd.Grouper(key='publish_time', axis=0, freq='D')]).sum()
  df_video_trend = pd.DataFrame(df_video_trend.to_records())
  fig = px.line(df_video_trend, x='publish_time', y='likes', color='category_id')
  return fig

def drawDislikeVideoTrend(df_subset):
  df_video_trend = df_subset.groupby(['category_id',pd.Grouper(key='publish_time', axis=0, freq='D')]).sum()
  df_video_trend = pd.DataFrame(df_video_trend.to_records())
  fig = px.line(df_video_trend, x='publish_time', y='dislikes', color='category_id')
  return fig

def drawCommentVideoTrend(df_subset):
  df_video_trend = df_subset.groupby(['category_id',pd.Grouper(key='publish_time', axis=0, freq='D')]).sum()
  df_video_trend = pd.DataFrame(df_video_trend.to_records())
  fig = px.line(df_video_trend, x='publish_time', y='comment_count', color='category_id')
  return fig


