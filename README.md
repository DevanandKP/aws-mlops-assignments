# aws-mlops-assignments

ASSIGNMENT 1
1.	Creating a folder in S3 bucket under the name (devanand.prakasa) with three folders A,B,C.
![image](https://user-images.githubusercontent.com/100085173/186853192-4980d61f-3356-46d5-8812-24fa3d61a29a.png)

2.	Uploaded files in each of the folders.

3.	Created a flask app to get the folder name and for reading the contents.
![image](https://user-images.githubusercontent.com/100085173/186853365-fbcc66b7-a57a-4312-b3ad-8a43f56e40f1.png)

4.	Tested the app in local.
![image](https://user-images.githubusercontent.com/100085173/186853443-bbf43a64-0998-48f2-9300-8a7150085843.png)

5.	Created an EC2 instance using t2.micro
![image](https://user-images.githubusercontent.com/100085173/186853528-56d7a809-25df-49ee-ac7e-b1d0b66c4584.png)

6.	Created and IAM Role and policy for accessing the s3 buckets and attached the same to the created ec2 instance.
![image](https://user-images.githubusercontent.com/100085173/186853614-a9380e81-5c02-490e-9f0c-9d4997b500ec.png)

7.	Configured the security group to allow incoming traffic through port 8085.
![image](https://user-images.githubusercontent.com/100085173/186853700-108d2951-041f-4e8d-b5e1-2fae7c2d6a17.png)

8.	Accessed the EC2 instance through SSH and used gunicorn to deploy the flask app on EC2 instance.
![image](https://user-images.githubusercontent.com/100085173/186853817-78ee2b76-7dcf-4b60-bbff-fd300f371054.png)

9.	Accessed the EC2-deployed flask app via the EC2-public URL at port 8085.
![image](https://user-images.githubusercontent.com/100085173/186853874-4b49ee0f-240e-4f57-81c4-616bc20ea311.png)


