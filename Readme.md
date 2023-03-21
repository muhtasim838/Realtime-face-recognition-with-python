# Real-time Face Recognition based Surveillance System

Real-time Face Recognition based Surveillance System uses [MS-FACE](https://azure.microsoft.com/en-in/services/cognitive-services/face/) API for face recognition based identification. It itentifies the unknown persons that are not registered and stores their images in a folder named unknown with current date and time. So it can be used for surviellance for security purposes as we can view all the unknown persons (besides staff) that visited a particular place on given date and time-interval. It consists of two apps register(register.py) and main(main.py) where register app is used to register new users and main.py is used for surveillance.  

### New User Registration
Register app is used to register the new user. Fisrt the information of new user is added to sqlite3 database (users.db). Then a personid is created for new person using MSFace APIs. Opencv2 with ***haarcascade classifier*** is used to extract the face from the captured images. After taking 8 face images for training these images are uploaded to cloudinary and added to MSFace APIs using *add_person_face* api calls. After uploading dataset to MSFace a model is build and trained so that it can identify the new person.

#### Steps for Registeration of a new person
1. Run register.py file using ```python register.py```. It will open pyqt GUI window.
2. Edit the details of users to be registered.
3. Click Verify Data button.
4. Click Create User button if verification is successful. This will create user entry in database and create the new person id in MSFace API.
5. Go to Generate face dataset tab.
6. Click Start button to start the camera.
7. Take 8 snapshot of face at different angles to train the model.
8. Click Upload Dataset button to upload face images to cloudinary and send their links in MSFace API calls.
9. Click train model to train the face identification model for given person.
10. Close the register.py window register is now complete.

## Overall Architecture of the System
![6](https://user-images.githubusercontent.com/42670033/226665941-3d26156d-4be1-425b-9718-0a3aa0599599.png)
<img src="https://user-images.githubusercontent.com/42670033/226665941-3d26156d-4be1-425b-9718-0a3aa0599599.png" width="150" height="280">

## Create New User
![5](https://user-images.githubusercontent.com/42670033/226666210-c1e93285-9c20-4f1f-b13c-3a91c3dfc23b.png)
![3](https://user-images.githubusercontent.com/42670033/226666236-efc44d65-366f-4782-8eb7-5aee38d9907f.png)

## Train New Faces
![1](https://user-images.githubusercontent.com/42670033/226666298-de51a000-4a49-4b4c-b398-75172a443dc8.png)

## Registration process
https://user-images.githubusercontent.com/42670033/226664300-9edca903-303e-4abe-b627-92f14ec29e23.mp4

### Surveillance
Surveillance app takes images at a regular time interval defined by *detection_interval* in ms (default value=10000, means 10 seconds). After taking images it extract all faces from the images using ***haarcascade classifier***  in opencv2. These face images are then uploaded to cloudinary and the cloudinary link is passed with api request to msface api. Two requests are send for a face identification first to add the face and generate a *face_id* and second to get *person_id* from the *face_id*. The *person_id* is used to get the information of the person from sqlite3 database (users.db). A green rectangle is drawn around the identified persons faces with there name while for unidentified persons a red rectangle is drawn with Unknown as their names. faces of all unknown persons are stored in *Unknowns* folder in the main directory with the current date and time which can be checked later for surveillance.

![4](https://user-images.githubusercontent.com/42670033/226666367-7356356b-ef5a-4b01-991f-6e23234930a8.png)

## Language used

 Python 2.7

## Required Python Libraries
 1. Opencv2
 2. PtQt4
 4. Configparser
 5. Cloudinary
 
 ### Installing required libraries
 1. Opencv2
  * **Ubuntu/Linux** ```sudo apt-get install python-opencv```
  * **Windows** follow [this link](http://opencvpython.blogspot.in/2012/05/install-opencv-in-windows-for-python.html)
    
 2. pip for python2.7
  * **Ubuntu/Linux** ```sudo apt-get install python-pip```
  * **Windows** Download [get-pip.py](https://bootstrap.pypa.io/get-pip.py). Then run ```python get-pip.py```
 
 3. PyQt4
  * **Ubuntu/Linux** ```sudo apt-get install python-qt4``` 
  * **Windows**  Download pyqt4 wheel file from [this link](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyqt4) (Download cp27 file for python2.7) Then Run ```pip install wheel_file_name``` like ```pip install PyQt4-4.11.4-cp27-none-win_amd64.whl```
        
 4. Configparser <br/>
  Run ```pip install configparser```
    
 5. Cloudinary <br/>
  Run ```pip install cloudinary```
  
## APIs used
 1. Microsoft Cognitive Services Face APIs (for building face identification model)
 2. Cloudinary APIs (for storing dataset)
 
### Setting up the APIs (Required for running project)
#### MSFace API
 1. Register for [MSFace API](https://azure.microsoft.com/en-in/services/cognitive-services/face/).
 2. Put the API Key in cnf.ini file in place of MSFACE_API_KEY.
 3. Replace *msface_api_url* in **MSFaceAPI.py** with your api base url.
 4. Go to MSFace API Reference. ([link](https://westus.dev.cognitive.microsoft.com/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236))
 5. Select Create under PersonGroup from left hand menu.
 6. Select your API testing console.
 7. Put **users** in personGroupId and API Key in Ocp-Apim-Subscription-Key. Then click send button. It will create a person group with name users which stores the resistered persons face data.
 
#### Cloudinary API
 1. Register for Cloudinary APIs. ([link](https://cloudinary.com/users/register/free))
 2. Go to console. ([link](https://cloudinary.com/console))
 3. Put cloud name, api key and api secret in cfg.ini file.
 4. Create a folder for project named RTFRSS (or whaever you want to name it)
 5. Create two subfolders in RTFRSS named dataset and tmp
 6. Replace *cloudinary_dataset* and *cloudinary_tmp* in **register.py** and **main.py** with your cloudinary project dataset and tmp folder paths.
 
