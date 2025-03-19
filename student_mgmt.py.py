import pymongo
client=pymongo.MongoClient("mongodb+srv://Project:ProjectDB@cluster0.wlvqw.mongodb.net/",tlsAllowInvalidCertificates=True);

myDB=client["ducat"];
coll = myDB.student;
coll1 = myDB.placed;

def admission(ducat_id,st_name,c_name,duration):
    coll.insert_one({"id":ducat_id,"name":st_name,"course":c_name,"duration":duration,"status":"Incomplete"});
    print("\n✅ Data Saved\n")

def total():
    for el in coll.find():
        print("*"*35)
        print(f"Ducat-Id: {el['id']}\nName: {el['name']}\nCourse: {el['course']}\nDuration: {el['duration']}");
        print("*"*35)

def extension(ducat_id,duration):
    coll.update_one({"id":ducat_id},{"$inc":{"duration":duration}});
    print("\n⏱️ Course Extended\n");
    
def placed(ducat_id,name,course):
    coll1.insert_one({"id":ducat_id, "name":name, "course":course});
    print("\n🚀 Placed Student Record Inserted\n")

def certificate(ducat_id):
    for el in coll.find({"id":ducat_id}):
        if(el["status"]=="Completed"):
            print("🏆 Certificate Permitted");
        elif(el["status"]!="Completed"):
            print("⚠️ Course is Incomplete. Please talk to your Counsellor");
        else:
            print("❌ Invalid user");

def delete(ducat_id):
    coll.delete_one({"id":ducat_id});
    print("\n🗑️  Record Deleted\n");
    
def updateofStatus(ducat_id,currentStatus):
    coll.update_one({"id":ducat_id},{"$set":{"status":currentStatus}});
    print("\n🔄 Status of course updated\n");

def placedlist():
    for el in coll1.find():
        print("*"*35)
        print(f"Ducat-Id: {el['id']}\nName: {el['name']}\nCourse: {el['course']}");
        print("*"*35)

def main():
    while(True):
        print("\n📚 Ducat Database Operations:");
        print("1️⃣  Press 1 for New Admission");
        print("2️⃣  Press 2 for Total Students");
        print("3️⃣  Press 3 for Extension of Course");
        print("4️⃣  Press 4 for Insert Placed Student Record");
        print("5️⃣  Press 5 for Certificate of Course");
        print("6️⃣  Press 6 for Delete a Record");
        print("7️⃣  Press 7 for Updation of Status");
        print("8️⃣  Press 8 for List of Placed Students");
        print("9️⃣  Press 9 for Exit from Database");

        try:
            choice = int(input("🔍 Enter the Operation: "));
        except ValueError:
            print("❌ Invalid input! Please enter a number between 1 and 9.");
            continue;

        if(choice==1):
            '''ducat_id,st_name,c_name,duraion,status'''
            try:
                ducat_id = int(input("🆔 Enter Id: "));
                st_name = input("👤 Enter Name: ");
                c_name = input("📘 Enter Course Name: ");
                duration = int(input("⏳ Enter Total Months: "));
                admission(ducat_id, st_name, c_name, duration);
            except ValueError:
                print("❌ Please enter a valid number for Id and Duration.");
        elif(choice==2):
            total();
        elif(choice==3):
            try:
                ducat_id = int(input("🆔 Enter Ducat Id: "));
                duration = int(input("⏱️ Enter the duration to extend: "));
                extension(ducat_id, duration);
            except ValueError:
                print("❌ Please enter a valid number for Id and Duration.");
        elif(choice==4):
            try:
                ducat_id = int(input("🆔 Enter Ducat Id: "));
                name = input("👤 Enter Name: ");
                course = input("📘 Enter the course: ");
                placed(ducat_id, name, course);
            except ValueError:
                print("❌ Please enter a valid number for Id.");
        elif(choice==5):
            try:
                ducat_id = int(input("🆔 Enter Ducat Id: "));
                certificate(ducat_id);
            except ValueError:
                print("❌ Please enter a valid number for Id.");
        elif(choice==6):
            try:
                ducat_id = int(input("🆔 Enter Id to delete: "));
                delete(ducat_id);
            except ValueError:
                print("❌ Please enter a valid number for Id.");
        elif(choice==7):
            try:
                ducat_id = int(input("🆔 Enter Id to update: "));
                status = input("🔄 Enter current status of course: ");
                updateofStatus(ducat_id, status);
            except ValueError:
                print("❌ Please enter a valid number for Id.");
        elif(choice==8):
            placedlist();
        elif(choice==9):
            print("👋 Exiting Database. Goodbye!")
            break;
        else:
            print("❌ Invalid Operation")

if __name__=="__main__":
    main()

