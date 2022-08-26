import boto3
from flask import Flask, render_template

app = Flask(__name__)

def listbucket():
    s3 = boto3.resource('s3')

    my_bucket = s3.Bucket('tiger-mle-pg')

    li=[]

    for my_bucket_object in my_bucket.objects.filter(Prefix="home/devanand.prakasa/"):
        if my_bucket_object.key !="home/devanand.prakasa/":
            li.append(my_bucket_object.key)
    return li

@app.route('/')
def home():
    
    objectlist=listbucket()
    return render_template('home.html', bucketlist=objectlist)

if __name__ == '__main__':
   app.run()

