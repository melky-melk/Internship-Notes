using System;
using Android.App;
using Android.OS;
using AndroidX.AppCompat.Widget;
using Training_Rooms;

namespace trainingroom.droid
{
    [Activity(Label = "trainingrooms.droid", Theme = "@style/AppTheme.NoActionBar", MainLauncher = true)]
    [Obsolete]
    public class MainActivity : ListActivity
    {

        protected override void OnCreate(Bundle savedInstanceState)
        {
            base.OnCreate(savedInstanceState);
            SetContentView(Resource.Layout.content_main);

            var repo = new RoomRepository();
            var rooms = repo.GetRooms();

            //gets all the rooms from the room repository class and displays it onto the screen according to the layout
            var adapter = new Android.Widget.ArrayAdapter<TrainingRoom>(this, Resource.Layout.RoomListItem, rooms.ToArray());

            this.ListAdapter = adapter;
        }
    }
}
