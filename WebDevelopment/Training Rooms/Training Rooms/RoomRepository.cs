using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Training_Rooms
{
    public class RoomRepository
    {
        private List<TrainingRoom> _rooms = new List<TrainingRoom> {
            new TrainingRoom() {
                Id = 1,
                Name = "Copernicus",
                Location = "building 1",
                NumberComputers = 25
            },
            new TrainingRoom() {
                Id = 2,
                Name = "Lemon",
                Location = "Francis Kearny",
                NumberComputers = 0
            },
            new TrainingRoom() {
                Id = 3,
                Name = "beab",
                Location = "University Lane",
                NumberComputers = 30
            },
        };

        public List<TrainingRoom> GetRooms()
        {
            return null;
        }

        public TrainingRoom GetRoom(int id)
        {
            return (from r in _rooms
             where r.Id == id
             select r).FirstOrDefault();

        }
    }

    
}
