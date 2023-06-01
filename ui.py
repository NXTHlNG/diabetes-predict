import tkinter
import tkinter.messagebox
from PIL import Image, ImageTk
import os
import customtkinter
import ml


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Diabetes Predict")
        self.geometry("700x700")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="Diabetes Predict",  # image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Predict",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="History",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        # self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image)
        # self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.age_input_frame = customtkinter.CTkFrame(master=self.home_frame, fg_color="transparent")
        self.age_input_frame.grid(row=0, column=0, padx=(20, 20), pady=(10, 0), sticky="nsew")
        self.age_input_label = customtkinter.CTkLabel(master=self.age_input_frame, text="Age: ")
        self.age_input_label.grid(row=0, column=0, columnspan=1, padx=10, pady=0, sticky="nw")
        self.age_entry = customtkinter.CTkEntry(master=self.age_input_frame,
                                                placeholder_text="Type age")
        self.age_entry.grid(row=1, column=0, padx=10, pady=0, sticky="nw")

        self.height_input_frame = customtkinter.CTkFrame(master=self.home_frame, fg_color="transparent")
        self.height_input_frame.grid(row=1, column=0, padx=(20, 20), pady=(10, 0), sticky="nsew")
        self.height_input_frame_input_label = customtkinter.CTkLabel(master=self.height_input_frame, text="Height: ")
        self.height_input_frame_input_label.grid(row=0, column=0, columnspan=1, padx=10, pady=0, sticky="nw")
        self.height_entry = customtkinter.CTkEntry(master=self.height_input_frame,
                                                   placeholder_text="Type height")
        self.height_entry.grid(row=1, column=0, padx=10, pady=0, sticky="nw")

        self.weight_input_frame = customtkinter.CTkFrame(master=self.home_frame, fg_color="transparent")
        self.weight_input_frame.grid(row=2, column=0, padx=(20, 20), pady=(10, 0), sticky="nsew")
        self.weight_input_frame_input_label = customtkinter.CTkLabel(master=self.weight_input_frame, text="Weight: ")
        self.weight_input_frame_input_label.grid(row=0, column=0, columnspan=1, padx=10, pady=0, sticky="nw")
        self.weight_entry = customtkinter.CTkEntry(master=self.weight_input_frame,
                                                   placeholder_text="Type weight")
        self.weight_entry.grid(row=1, column=0, padx=10, pady=0, sticky="nw")

        self.HbA1c_input_frame = customtkinter.CTkFrame(master=self.home_frame, fg_color="transparent")
        self.HbA1c_input_frame.grid(row=3, column=0, padx=(20, 20), pady=(10, 0), sticky="nsew")
        self.HbA1c_input_frame_input_label = customtkinter.CTkLabel(master=self.HbA1c_input_frame, text="HbA1c level: ")
        self.HbA1c_input_frame_input_label.grid(row=0, column=0, columnspan=1, padx=10, pady=0, sticky="nw")
        self.entry_HbA1c = customtkinter.CTkEntry(master=self.HbA1c_input_frame,
                                                  placeholder_text="Type HbA1c level")
        self.entry_HbA1c.grid(row=1, column=0, padx=10, pady=0, sticky="nw")

        self.glucose_input_frame = customtkinter.CTkFrame(master=self.home_frame, fg_color="transparent")
        self.glucose_input_frame.grid(row=4, column=0, padx=(20, 20), pady=(10, 0), sticky="nsew")
        self.glucose_input_frame_input_label = customtkinter.CTkLabel(master=self.glucose_input_frame, text="Glucose level: ")
        self.glucose_input_frame_input_label.grid(row=0, column=0, columnspan=1, padx=10, pady=0, sticky="nw")
        self.entry_glucose = customtkinter.CTkEntry(master=self.glucose_input_frame,
                                                    placeholder_text="Type glucose level")
        self.entry_glucose.grid(row=1, column=0, padx=10, pady=0, sticky="nw")

        self.radiobutton_gender_frame = customtkinter.CTkFrame(master=self.home_frame, fg_color="transparent")
        self.radiobutton_gender_frame.grid(row=5, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.gender_var = tkinter.StringVar(value="Male")
        self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_gender_frame, text="Gender: ")
        self.label_radio_group.grid(row=0, column=0, columnspan=1, padx=10, pady=0, sticky="nw")
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_gender_frame, text="Male", variable=self.gender_var, value="Male")
        self.radio_button_1.grid(row=1, column=0, pady=0, padx=10, sticky="n")
        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_gender_frame, text="Female", variable=self.gender_var, value="Female")
        self.radio_button_2.grid(row=1, column=1, pady=0, padx=10, sticky="n")

        self.hypertension_input_frame = customtkinter.CTkFrame(master=self.home_frame, fg_color="transparent")
        self.hypertension_input_frame.grid(row=6, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.hypertension_input_label = customtkinter.CTkLabel(master=self.hypertension_input_frame, text="Diseases: ")
        self.hypertension_input_label.grid(row=0, column=0, columnspan=1, padx=10, pady=0, sticky="nw")
        self.hypertension_checkbox = customtkinter.CTkCheckBox(master=self.hypertension_input_frame, text="Hypertension")
        self.hypertension_checkbox.grid(row=1, column=0, pady=0, padx=10, sticky="n")
        self.heart_disease_checkbox = customtkinter.CTkCheckBox(master=self.hypertension_input_frame, text="Heart Disease")
        self.heart_disease_checkbox.grid(row=1, column=1, pady=0, padx=10, sticky="n")

        self.radiobutton_smoke_frame = customtkinter.CTkFrame(master=self.home_frame, fg_color="transparent")
        self.radiobutton_smoke_frame.grid(row=7, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.smoke_var = tkinter.StringVar(value="never")
        self.label_smoke_group = customtkinter.CTkLabel(master=self.radiobutton_smoke_frame, text="Smoking History: ")
        self.label_smoke_group.grid(row=0, column=0, columnspan=1, padx=10, pady=0, sticky="nw")
        self.radio_smoke_1 = customtkinter.CTkRadioButton(master=self.radiobutton_smoke_frame, text="Never", variable=self.smoke_var, value="non-smoker")
        self.radio_smoke_1.grid(row=1, column=0, pady=0, padx=10, sticky="n")
        self.radio_smoke_2 = customtkinter.CTkRadioButton(master=self.radiobutton_smoke_frame, text="Ever", variable=self.smoke_var, value="past_smoker")
        self.radio_smoke_2.grid(row=1, column=1, pady=0, padx=10, sticky="n")
        self.radio_smoke_3 = customtkinter.CTkRadioButton(master=self.radiobutton_smoke_frame, text="Current", variable=self.smoke_var, value="current")
        self.radio_smoke_3.grid(row=1, column=2, pady=0, padx=10, sticky="n")

        self.predict_button = customtkinter.CTkButton(master=self.home_frame, text="Predict", command=self.predict)
        self.predict_button.grid(row=8, column=0, padx=30, pady=(10, 0), sticky="nsew")

        self.result_label = customtkinter.CTkLabel(master=self.home_frame, text="Result: ", font=customtkinter.CTkFont(size=16))
        self.result_label.grid(row=9, column=0, columnspan=1, padx=30, pady=10, sticky="nw")

        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("home")

    def predict(self):
        age = int(self.age_entry.get())
        gender = self.gender_var.get()
        weight = int(self.weight_entry.get())
        height = int(self.height_entry.get())
        hypertension = self.hypertension_checkbox.get()
        heart_disease = self.heart_disease_checkbox.get()
        smoking_history = self.smoke_var.get()
        HbA1c_level = float(self.entry_HbA1c.get())
        blood_glucose_level = int(self.entry_glucose.get())
        bmi = float(toFixed(weight / (height ** 2) * 10000, 2))
        result = bool(ml.predict(age, gender, hypertension, heart_disease, smoking_history, HbA1c_level, blood_glucose_level, bmi))
        if result:
            self.result_label.configure("Result: Risk")
        else:
            self.result_label.configure("Result: No Risk")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


if __name__ == "__main__":
    app = App()
    app.mainloop()
