import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class FitnessApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fitness Tracker")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')
        
        # Create main container
        self.main_frame = tk.Frame(root, bg='#f0f0f0')
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Create notebook (tabs)
        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Create tabs
        self.create_dashboard_tab()
        self.create_workout_tab()
        self.create_nutrition_tab()
        self.create_progress_tab()
        
        # Initialize data
        self.workouts = []
        self.meals = []
        self.weight_history = []
        
    def create_dashboard_tab(self):
        """Create the dashboard tab with summary information"""
        self.dashboard_tab = tk.Frame(self.notebook, bg='#f0f0f0')
        self.notebook.add(self.dashboard_tab, text="Dashboard")
        
        # Header
        header = tk.Label(self.dashboard_tab, text="Fitness Dashboard", font=('Helvetica', 18, 'bold'), bg='#f0f0f0')
        header.pack(pady=10)
        
        # Stats frame
        stats_frame = tk.Frame(self.dashboard_tab, bg='white', bd=2, relief=tk.GROOVE)
        stats_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Stats labels
        tk.Label(stats_frame, text="Today's Stats", font=('Helvetica', 12, 'bold'), bg='white').pack(pady=5)
        
        stats_grid = tk.Frame(stats_frame, bg='white')
        stats_grid.pack(pady=10)
        
        tk.Label(stats_grid, text="Workouts Completed:", bg='white').grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.workouts_completed_label = tk.Label(stats_grid, text="0", bg='white', fg='blue')
        self.workouts_completed_label.grid(row=0, column=1, padx=5, pady=5, sticky='w')
        
        tk.Label(stats_grid, text="Calories Consumed:", bg='white').grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.calories_consumed_label = tk.Label(stats_grid, text="0", bg='white', fg='green')
        self.calories_consumed_label.grid(row=1, column=1, padx=5, pady=5, sticky='w')
        
        tk.Label(stats_grid, text="Current Weight:", bg='white').grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.current_weight_label = tk.Label(stats_grid, text="-- kg", bg='white', fg='purple')
        self.current_weight_label.grid(row=2, column=1, padx=5, pady=5, sticky='w')
        
        # Recent activities
        activities_frame = tk.Frame(self.dashboard_tab, bg='white', bd=2, relief=tk.GROOVE)
        activities_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        tk.Label(activities_frame, text="Recent Activities", font=('Helvetica', 12, 'bold'), bg='white').pack(pady=5)
        
        self.activities_list = tk.Listbox(activities_frame, height=8)
        self.activities_list.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Add sample data
        self.activities_list.insert(tk.END, "No recent activities")
    
    def create_workout_tab(self):
        """Create the workout tracking tab"""
        self.workout_tab = tk.Frame(self.notebook, bg='#f0f0f0')
        self.notebook.add(self.workout_tab, text="Workouts")
        
        # Header
        header = tk.Label(self.workout_tab, text="Workout Tracker", font=('Helvetica', 18, 'bold'), bg='#f0f0f0')
        header.pack(pady=10)
        
        # Workout entry form
        form_frame = tk.Frame(self.workout_tab, bg='white', bd=2, relief=tk.GROOVE)
        form_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(form_frame, text="Add New Workout", font=('Helvetica', 12, 'bold'), bg='white').pack(pady=5)
        
        # Form fields
        fields_frame = tk.Frame(form_frame, bg='white')
        fields_frame.pack(pady=10)
        
        tk.Label(fields_frame, text="Workout Type:", bg='white').grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.workout_type = ttk.Combobox(fields_frame, values=["Running", "Cycling", "Weight Training", "Swimming", "Yoga"])
        self.workout_type.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(fields_frame, text="Duration (mins):", bg='white').grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.workout_duration = tk.Entry(fields_frame)
        self.workout_duration.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(fields_frame, text="Calories Burned:", bg='white').grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.workout_calories = tk.Entry(fields_frame)
        self.workout_calories.grid(row=2, column=1, padx=5, pady=5)
        
        tk.Label(fields_frame, text="Date:", bg='white').grid(row=3, column=0, padx=5, pady=5, sticky='e')
        self.workout_date = tk.Entry(fields_frame)
        self.workout_date.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.workout_date.grid(row=3, column=1, padx=5, pady=5)
        
        # Add button
        add_button = tk.Button(form_frame, text="Add Workout", command=self.add_workout, bg='#4CAF50', fg='white')
        add_button.pack(pady=10)
        
        # Workout history
        history_frame = tk.Frame(self.workout_tab, bg='white', bd=2, relief=tk.GROOVE)
        history_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        tk.Label(history_frame, text="Workout History", font=('Helvetica', 12, 'bold'), bg='white').pack(pady=5)
        
        # Treeview for workout history
        columns = ("Date", "Type", "Duration", "Calories")
        self.workout_tree = ttk.Treeview(history_frame, columns=columns, show="headings", height=10)
        
        for col in columns:
            self.workout_tree.heading(col, text=col)
            self.workout_tree.column(col, width=150, anchor=tk.CENTER)
        
        self.workout_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(history_frame, orient=tk.VERTICAL, command=self.workout_tree.yview)
        self.workout_tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    def create_nutrition_tab(self):
        """Create the nutrition tracking tab"""
        self.nutrition_tab = tk.Frame(self.notebook, bg='#f0f0f0')
        self.notebook.add(self.nutrition_tab, text="Nutrition")
        
        # Header
        header = tk.Label(self.nutrition_tab, text="Nutrition Tracker", font=('Helvetica', 18, 'bold'), bg='#f0f0f0')
        header.pack(pady=10)
        
        # Nutrition entry form
        form_frame = tk.Frame(self.nutrition_tab, bg='white', bd=2, relief=tk.GROOVE)
        form_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(form_frame, text="Add Meal/Food", font=('Helvetica', 12, 'bold'), bg='white').pack(pady=5)
        
        # Form fields
        fields_frame = tk.Frame(form_frame, bg='white')
        fields_frame.pack(pady=10)
        
        tk.Label(fields_frame, text="Meal Type:", bg='white').grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.meal_type = ttk.Combobox(fields_frame, values=["Breakfast", "Lunch", "Dinner", "Snack"])
        self.meal_type.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(fields_frame, text="Food Item:", bg='white').grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.food_item = tk.Entry(fields_frame)
        self.food_item.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(fields_frame, text="Calories:", bg='white').grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.meal_calories = tk.Entry(fields_frame)
        self.meal_calories.grid(row=2, column=1, padx=5, pady=5)
        
        tk.Label(fields_frame, text="Protein (g):", bg='white').grid(row=3, column=0, padx=5, pady=5, sticky='e')
        self.meal_protein = tk.Entry(fields_frame)
        self.meal_protein.grid(row=3, column=1, padx=5, pady=5)
        
        tk.Label(fields_frame, text="Date:", bg='white').grid(row=4, column=0, padx=5, pady=5, sticky='e')
        self.meal_date = tk.Entry(fields_frame)
        self.meal_date.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.meal_date.grid(row=4, column=1, padx=5, pady=5)
        
        # Add button
        add_button = tk.Button(form_frame, text="Add Meal", command=self.add_meal, bg='#4CAF50', fg='white')
        add_button.pack(pady=10)
        
        # Meal history
        history_frame = tk.Frame(self.nutrition_tab, bg='white', bd=2, relief=tk.GROOVE)
        history_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        tk.Label(history_frame, text="Meal History", font=('Helvetica', 12, 'bold'), bg='white').pack(pady=5)
        
        # Treeview for meal history
        columns = ("Date", "Meal Type", "Food Item", "Calories", "Protein")
        self.meal_tree = ttk.Treeview(history_frame, columns=columns, show="headings", height=10)
        
        for col in columns:
            self.meal_tree.heading(col, text=col)
            self.meal_tree.column(col, width=120, anchor=tk.CENTER)
        
        self.meal_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(history_frame, orient=tk.VERTICAL, command=self.meal_tree.yview)
        self.meal_tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    def create_progress_tab(self):
        """Create the progress tracking tab"""
        self.progress_tab = tk.Frame(self.notebook, bg='#f0f0f0')
        self.notebook.add(self.progress_tab, text="Progress")
        
        # Header
        header = tk.Label(self.progress_tab, text="Progress Tracker", font=('Helvetica', 18, 'bold'), bg='#f0f0f0')
        header.pack(pady=10)
        
        # Weight tracking
        weight_frame = tk.Frame(self.progress_tab, bg='white', bd=2, relief=tk.GROOVE)
        weight_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(weight_frame, text="Weight Tracking", font=('Helvetica', 12, 'bold'), bg='white').pack(pady=5)
        
        # Weight entry form
        form_frame = tk.Frame(weight_frame, bg='white')
        form_frame.pack(pady=10)
        
        tk.Label(form_frame, text="Current Weight (kg):", bg='white').grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.current_weight = tk.Entry(form_frame)
        self.current_weight.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(form_frame, text="Date:", bg='white').grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.weight_date = tk.Entry(form_frame)
        self.weight_date.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.weight_date.grid(row=1, column=1, padx=5, pady=5)
        
        # Add button
        add_button = tk.Button(weight_frame, text="Record Weight", command=self.record_weight, bg='#4CAF50', fg='white')
        add_button.pack(pady=10)
        
        # Weight history
        history_frame = tk.Frame(self.progress_tab, bg='white', bd=2, relief=tk.GROOVE)
        history_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        tk.Label(history_frame, text="Weight History", font=('Helvetica', 12, 'bold'), bg='white').pack(pady=5)
        
        # Treeview for weight history
        columns = ("Date", "Weight (kg)")
        self.weight_tree = ttk.Treeview(history_frame, columns=columns, show="headings", height=10)
        
        for col in columns:
            self.weight_tree.heading(col, text=col)
            self.weight_tree.column(col, width=200, anchor=tk.CENTER)
        
        self.weight_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(history_frame, orient=tk.VERTICAL, command=self.weight_tree.yview)
        self.weight_tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Add chart placeholder
        chart_frame = tk.Frame(self.progress_tab, bg='white', bd=2, relief=tk.GROOVE)
        chart_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        tk.Label(chart_frame, text="Progress Chart (placeholder)", bg='white').pack(pady=50)
    
    def add_workout(self):
        """Add a new workout to the tracker"""
        workout_type = self.workout_type.get()
        duration = self.workout_duration.get()
        calories = self.workout_calories.get()
        date = self.workout_date.get()
        
        if not all([workout_type, duration, calories, date]):
            messagebox.showerror("Error", "Please fill in all fields")
            return
        
        try:
            duration = int(duration)
            calories = int(calories)
        except ValueError:
            messagebox.showerror("Error", "Duration and Calories must be numbers")
            return
        
        # Add to workouts list
        workout = {
            "type": workout_type,
            "duration": duration,
            "calories": calories,
            "date": date
        }
        self.workouts.append(workout)
        
        # Add to treeview
        self.workout_tree.insert("", tk.END, values=(date, workout_type, f"{duration} mins", calories))
        
        # Clear fields
        self.workout_type.set('')
        self.workout_duration.delete(0, tk.END)
        self.workout_calories.delete(0, tk.END)
        
        # Update dashboard
        self.update_dashboard()
        
        messagebox.showinfo("Success", "Workout added successfully!")
    
    def add_meal(self):
        """Add a new meal to the tracker"""
        meal_type = self.meal_type.get()
        food_item = self.food_item.get()
        calories = self.meal_calories.get()
        protein = self.meal_protein.get()
        date = self.meal_date.get()
        
        if not all([meal_type, food_item, calories, date]):
            messagebox.showerror("Error", "Please fill in all required fields")
            return
        
        try:
            calories = int(calories)
            protein = int(protein) if protein else 0
        except ValueError:
            messagebox.showerror("Error", "Calories and Protein must be numbers")
            return
        
        # Add to meals list
        meal = {
            "type": meal_type,
            "food": food_item,
            "calories": calories,
            "protein": protein,
            "date": date
        }
        self.meals.append(meal)
        
        # Add to treeview
        self.meal_tree.insert("", tk.END, values=(date, meal_type, food_item, calories, protein))
        
        # Clear fields
        self.meal_type.set('')
        self.food_item.delete(0, tk.END)
        self.meal_calories.delete(0, tk.END)
        self.meal_protein.delete(0, tk.END)
        
        # Update dashboard
        self.update_dashboard()
        
        messagebox.showinfo("Success", "Meal added successfully!")
    
    def record_weight(self):
        """Record current weight"""
        weight = self.current_weight.get()
        date = self.weight_date.get()
        
        if not all([weight, date]):
            messagebox.showerror("Error", "Please fill in all fields")
            return
        
        try:
            weight = float(weight)
        except ValueError:
            messagebox.showerror("Error", "Weight must be a number")
            return
        
        # Add to weight history
        self.weight_history.append({
            "weight": weight,
            "date": date
        })
        
        # Add to treeview
        self.weight_tree.insert("", tk.END, values=(date, weight))
        
        # Clear field
        self.current_weight.delete(0, tk.END)
        
        # Update dashboard
        self.update_dashboard()
        
        messagebox.showinfo("Success", "Weight recorded successfully!")
    
    def update_dashboard(self):
        """Update the dashboard with current data"""
        # Update workouts completed
        today = datetime.now().strftime("%Y-%m-%d")
        today_workouts = [w for w in self.workouts if w["date"] == today]
        self.workouts_completed_label.config(text=str(len(today_workouts)))
        
        # Update calories consumed
        today_meals = [m for m in self.meals if m["date"] == today]
        total_calories = sum(m["calories"] for m in today_meals)
        self.calories_consumed_label.config(text=f"{total_calories} kcal")
        
        # Update current weight
        if self.weight_history:
            latest_weight = self.weight_history[-1]["weight"]
            self.current_weight_label.config(text=f"{latest_weight} kg")
        
        # Update recent activities
        self.activities_list.delete(0, tk.END)
        
        # Get recent workouts and meals (last 5 of each)
        recent_workouts = self.workouts[-5:] if len(self.workouts) > 5 else self.workouts
        recent_meals = self.meals[-5:] if len(self.meals) > 5 else self.meals
        
        # Combine and sort by date
        recent_activities = []
        for workout in recent_workouts:
            recent_activities.append((workout["date"], f"Workout: {workout['type']} ({workout['duration']} mins)"))
        
        for meal in recent_meals:
            recent_activities.append((meal["date"], f"Meal: {meal['type']} - {meal['food']}"))
        
        # Sort by date (newest first)
        recent_activities.sort(key=lambda x: x[0], reverse=True)
        
        # Add to listbox
        if recent_activities:
            for activity in recent_activities:
                self.activities_list.insert(tk.END, activity[1])
        else:
            self.activities_list.insert(tk.END, "No recent activities")

if __name__ == "__main__":
    root = tk.Tk()
    app = FitnessApp(root)
    root.mainloop()