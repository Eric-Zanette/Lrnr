import { useEffect, useState } from "react";
import { hourList, dayList } from "../utilties";

const Schedule = () => {
  const [schedule, setSchedule] = useState({});

  useEffect(() => {
    const get_schedule = async () => {
      const response = await fetch("/api/schedule", {
        method: "POST",
        headers: {
          Accept: "applicaton/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ topic: "chess", level: "beginner" }),
      });
      const data = await response.json();
      setSchedule(data);
    };
    get_schedule();
  }, []);

  return (
    <div className="scheduleContainer">
      <div className="schedule">
        {dayList.map((day) => {
          return (
            <div className="dayContainer" key={day}>
              <p>{day}</p>
              {hourList.map((hour) => {
                return <div className={`timeSlot ${day} ${hour}`}></div>;
              })}
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default Schedule;
