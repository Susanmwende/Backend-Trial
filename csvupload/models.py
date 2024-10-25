from django.db import models



class School(models.Model):
    code = models.CharField(max_length=100)
    school_name = models.CharField(max_length=255)
    level = models.CharField(max_length=100)
    school_status = models.CharField(max_length=100)
    school_type = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    sub_county = models.CharField(max_length=100)
    division = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    constituency = models.CharField(max_length=100)

    def __str__(self):
        return self.school_name

import React, { useState } from 'react';

const Palette = ({ onIconSelect }) => {
  const categories = [
    {
      id: 'agriculture',
      title: 'Agriculture',
      icon: '🌾',
      icons: [
        '🚜', '🌻', '👨‍🌾', '🐄', '🍎', '🥕', '🌽', '🐑', '🐓', '🍇',
        '🍞', '🌿', '🍠', '🧄', '🧅', '🍒', '🍓', '🥭', '🥥', '🍋',
        '🍉', '🍊', '🍍', '🥬', '🥒', '🧑‍🌾', '🍑', '🌸', '🌷', '🥔'
      ],
    },
    {
      id: 'modeling',
      title: 'Modeling (Clay)',
      icon: '🏺',
      icons: [
        '🎨', '🖌️', '🧱', '🖼️', '🧑‍🎨', '🧑‍🏭', '🎭', '👩‍🎨', '🧑‍🎤', '🎬',
        '🖍️', '🖊️', '🧶', '🧵', '📐', '📏', '🎴', '✂️', '🧩', '🖼️',
        '🎭', '🧑‍🎨', '🎨', '🖌️', '🎨', '🧑‍🏭', '🎭', '🧩', '🖍️', '📐'
      ],
    },
    {
      id: 'environment',
      title: 'Environment',
      icon: '🌍',
      icons: [
        '🌱', '🍃', '🌳', '♻️', '💧', '🌤', '🌊', '🏞', '🦜', '🌿',
        '🌵', '🍂', '🌾', '🏔', '🌋', '🍄', '🦋', '🪲', '🐝', '🐛',
        '🐞', '🦚', '🌸', '🌷', '🍀', '🐾', '🐦', '🦥', '🍁', '🦥'
      ],
    },
    {
      id: 'art_and_craft',
      title: 'Art and Craft',
      icon: '✂️',
      icons: [
        '✂️', '🧵', '🖍️', '🧷', '🧩', '📏', '🖊️', '📐', '🖌️', '🧶',
        '🧑‍🎨', '🎨', '🎭', '🎬', '🎨', '🧑‍🏭', '🧩', '📏', '📐', '🎴',
        '📎', '📓', '🖇', '📖', '🧵', '🖼', '🖍', '🎭', '🧷', '📚'
      ],
    },
    {
      id: 'knitting',
      title: 'Knitting',
      icon: '🧶',
      icons: [
        '🧣', '🧷', '👕', '🧤', '🧢', '🧦', '🧵', '👒', '👗', '👚',
        '🧥', '👔', '👘', '🧤', '🧵', '🧷', '🧣', '🧦', '🧑‍🎨', '🧥',
        '🧑‍🎨', '🧤', '🧣', '🧶', '✂️', '📏', '🧑‍🎨', '📐', '📎', '🧵'
      ],
    },
    {
      id: 'cooking',
      title: 'Cooking',
      icon: '🍳',
      icons: [
        '🍔', '🥘', '🍕', '🍜', '🍱', '🍝', '🥗', '🍲', '🍰', '🍣',
        '🍤', '🍩', '🥞', '🍴', '🍇', '🍧', '🍮', '🍫', '🍿', '🥐',
        '🍔', '🍟', '🍖', '🍗', '🥓', '🍞', '🍍', '🍤', '🔪', '🍴', '🥄', 
        '🍽', '🧂', '🍶', '🍯', '🍶', '🥢', '🍚', '🫖', '🍵'
      ],
    },
  ];

  const [selectedCategory, setSelectedCategory] = useState(categories[0].id);

  const handleCategoryChange = (categoryId) => {
    setSelectedCategory(categoryId);
  };
  
  const activeCategory = categories.find((cat) => cat.id === selectedCategory);
  
  return (
    <div 
      className="bg-pink-100 text-white rounded-lg shadow-lg p-4 w-full h-auto" // Full width and auto height
      style={{ margin: 0, padding: 0 }} // Remove any default margins/padding
    >
      <h2 className="text-xl font-bold text-center mb-3">Select an Icon</h2>
      
      {/* Category Selection */}
      <div className="flex justify-around mb-3 bg-pink-100 w-full"> {/* Ensure full width */}
        {categories.map((category) => (
          <div
            key={category.id}
            className={`flex flex-col items-center cursor-pointer p-2 rounded-lg 
              ${category.id === selectedCategory ? 'bg-[#644877]' : 
                'bg-[#A083C9] hover:bg-[#644877]'}`}
            onClick={() => handleCategoryChange(category.id)}
            style={{ width: '10%' }}  // Keep this for category items
          >
            <span className="text-6xl">{category.icon}</span>
            <span className="text-md font-medium">{category.title}</span>
          </div>
        ))}
      </div>
  
      {/* Icons Grid */}
      <div className="grid grid-cols-5 gap-4 bg-pink-100 w-full"> {/* Full width for icons grid */}
        {activeCategory.icons.map((icon, index) => (
          <div
            key={index}
            className="text-center bg-pink-200 cursor-pointer p-4 rounded-lg transition-colors duration-200 
              hover:bg-[#644877]"
            onClick={() => onIconSelect(icon)} // Call function to add icon
          >
            <span className="text-5xl">{icon}</span>
          </div>
        ))}
      </div>
    </div>
  );
  
  };
  
export default Palette;





'use client';
import React, { useEffect, useState, useRef } from 'react';

const KnittingUI = ({ togglePalette, selectedItems, isRecording, toggleRecording }) => {
  const [activeItemIndex, setActiveItemIndex] = useState(0);
  const [recordingProgress, setRecordingProgress] = useState(0); // Track progress
  const [isSaving, setIsSaving] = useState(false); // Track saving state
  const screenStreamRef = useRef(null);
  const mediaRecorderRef = useRef(null);
  const recordedChunks = useRef([]);
  const recordingIntervalRef = useRef(null); // Interval for tracking progress

  const totalRecordingTime = useRef(0); // Total duration of recording in seconds

  // Function to start recording the current screen
  const startScreenRecording = async () => {
    try {
      const stream = await navigator.mediaDevices.getDisplayMedia({ video: true }); // Capture the screen
      screenStreamRef.current = stream;

      mediaRecorderRef.current = new MediaRecorder(stream, {
        mimeType: 'video/webm',
      });

      mediaRecorderRef.current.ondataavailable = (event) => {
        if (event.data.size > 0) {
          recordedChunks.current.push(event.data);
        }
      };

      mediaRecorderRef.current.onstop = () => {
        const blob = new Blob(recordedChunks.current, { type: 'video/webm' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.style.display = 'none';
        a.href = url;
        a.download = 'screen-recording.webm';
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
        setIsSaving(false);
      };

      mediaRecorderRef.current.start();
      toggleRecording(); // Update recording state to true
      startProgressTracking(); // Start tracking recording progress
    } catch (err) {
      console.error('Error starting screen recording:', err);
    }
  };

  // Function to stop the screen recording
  const stopScreenRecording = () => {
    mediaRecorderRef.current.stop();
    screenStreamRef.current.getTracks().forEach((track) => track.stop());
    toggleRecording(); // Update recording state to false
    clearInterval(recordingIntervalRef.current); // Stop progress tracking
    setRecordingProgress(100); // Set progress to 100% when recording stops
    setIsSaving(true); // Indicate saving state
  };

  // Function to track progress during recording
  const startProgressTracking = () => {
    totalRecordingTime.current = selectedItems.reduce((total, item) => total + item.time, 0);
    setRecordingProgress(0); // Reset progress at start

    recordingIntervalRef.current = setInterval(() => {
      setRecordingProgress((prevProgress) => {
        const newProgress = prevProgress + (100 / totalRecordingTime.current);
        return newProgress >= 100 ? 100 : newProgress;
      });
    }, 1000); // Update progress every second
  };

  // Handle switching between selected icons based on timer
  useEffect(() => {
    if (isRecording && selectedItems.length > 0) {
      const currentItem = selectedItems[activeItemIndex];
      
      const timer = setTimeout(() => {
        if (activeItemIndex < selectedItems.length - 1) {
          setActiveItemIndex(activeItemIndex + 1);
        } else {
          setActiveItemIndex(0); // Loop back to first item
        }
      }, currentItem.time * 1000);

      return () => clearTimeout(timer);
    } else {
      setActiveItemIndex(0);
    }
  }, [isRecording, activeItemIndex, selectedItems]);

  return (
    <div className="h-screen bg-white p-8">
      {/* Page Title Section */}
      <div className="flex flex-col mb-6">
        <h1 className="text-xl font-normal text-gray-900">Part 1</h1>
        <h2 className="text-3xl font-bold text-gray-700">The Needle</h2>
      </div>

      {/* Knitting Section */}
      <div className="bg-pink-100 rounded-lg p-8 mb-8 relative w-/5 h-3/5 mx-auto shadow-lg flex flex-col justify-between">
        <div>
          <h3 className="text-3xl font-bold mb-6 text-pink-800">Knitting Section</h3>
          <div className="flex justify-center mb-6">
            <div className="relative w-40 h-40 flex items-center justify-center">
              {isRecording && selectedItems[activeItemIndex] && (
                <div className={`w-full h-full flex items-center justify-center`}>
                  {selectedItems[activeItemIndex].icon}
                </div>
              )}
            </div>
          </div>
        </div>

        {/* Progress bar */}
     
        <div className="flex justify-center items-center space-x-4 mt-4">
          <button 
            onClick={isRecording ? stopScreenRecording : startScreenRecording}
            className={`w-12 h-12 rounded-full focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-purple-500 ${isRecording ? 'bg-red-500' : 'bg-purple-600'}`}
            aria-label={isRecording ? "Stop recording" : "Start recording"}
            disabled={isSaving} // Disable the button while saving
          >
            {isRecording ? "🛑" : "🎤"}
          </button>

          {/* Toggle Palette */}
          <button 
            onClick={togglePalette} 
            className="text-5xl focus:outline-none"
            aria-label="Toggle Palette"
          >
            😊
          </button>
        </div>
      </div>

      {/* Parts grid */}
      <div className="grid grid-cols-4 gap-1 mt-8">
        {['The Yarn', 'The Needle', 'Knitting', 'Outcome'].map((text, index) => (
          <div key={index} className="flex flex-col items-start">
            <div className="bg-purple-200 p-6 h-32 w-64 flex items-center justify-center mb-2 shadow-md"></div>
            <div className="text-lg text-black text-left">Part {index + 1}</div>
            <div className="text-xl font-semibold text-black text-left">{text}</div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default KnittingUI;

'use client';
import React, { useEffect, useState } from 'react';

// Define an interface for timer items
interface TimerItem {
  icon: string;
  time: number;
  remainingTime: number;
  completed: boolean; // Track if item is completed
}

const Sidebar = ({ selectedItems = [], onItemTimeChange, onItemTimeElapsed }) => {
  const [timers, setTimers] = useState<TimerItem[]>([]); // Specify type here

  // Initialize timers whenever new items are selected
  useEffect(() => {
    if (selectedItems.length > 0) {
      const newTimers: TimerItem[] = selectedItems.map((item) => ({
        ...item,
        remainingTime: item.time || 60, // Start with 60 seconds
        completed: false // Track if item is completed
      }));
      setTimers(newTimers);
    }
  }, [selectedItems]);

  // Countdown timer logic
  useEffect(() => {
    const intervalId = setInterval(() => {
      setTimers((prevTimers) =>
        prevTimers.map((item, index) => {
          if (item.remainingTime > 0) {
            return { ...item, remainingTime: item.remainingTime - 1 };
          } else {
            onItemTimeElapsed(index); // Notify parent about elapsed time
            return { ...item, remainingTime: item.remainingTime, completed: true }; // Mark as completed
          }
        })
      );
    }, 1000);

    return () => clearInterval(intervalId);
    
  }, [onItemTimeElapsed]);

  // Function to handle icon tap to remove it from the sidebar
  const handleIconTap = (index: number) => {
    setTimers((prev) => prev.filter((_, i) => i !== index));
  };

  return (
    <div className="w-80 bg-pink-100 p-4 flex flex-col items-center space-y-4 overflow-y-auto" style={{ maxHeight: '80vh', minHeight: '100vh' }}>
      <h2 className="text-lg font-bold text-black">Selected Items</h2>
      {timers.length === 0 && <p className="text-black">No items selected</p>}
      {timers.map((item, index) => (
        <div key={index} 
             className={`relative flex flex-col items-center mb-2 border-4 border-gray-300 rounded-lg p-2 ${item.completed ? 'bg-green-200 opacity-50' : 'bg-white'} shadow-md cursor-pointer`}
             onClick={() => handleIconTap(index)} // Tap to remove
        >
          {item.completed && (
            <div className="absolute top-1 left-1 text-green-600 text-lg">✅</div> // Tick mark for completed
          )}
          <div className={`text-5xl mb-1 ${item.completed ? 'opacity-50' : ''}`}>{item.icon}</div> {/* Bigger icon with dim effect */}
          <div className="text-xl text-black">
            {Math.floor(item.remainingTime / 60)}:{String(item.remainingTime % 60).padStart(2, '0')}
          </div> {/* Timer displaying minutes and seconds */}
          
          {/* Adjustable time input */}
          <input 
            type="number" 
            value={item.time} 
            min={1} 
            onChange={(e) => {
              const newValue = Math.max(1, Number(e.target.value)); // Ensure at least 1 second
              const updatedTimers = [...timers];
              updatedTimers[index].time = newValue;
              updatedTimers[index].remainingTime = newValue; // Reset remaining time
              setTimers(updatedTimers);
              onItemTimeChange(index, newValue); // Notify parent about time change
            }} 
            className="w-20 mt-1 text-center border border-gray-300 rounded-md"
          />
        </div>
      ))}
    </div>
  );
};

export default Sidebar;
