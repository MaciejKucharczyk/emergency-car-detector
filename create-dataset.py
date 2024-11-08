import pandas as pd
import os
import shutil

train_dir = 'dataset/Emergency_Vehicles/train'
val_dir = ''

def organize_files() -> None:
    # Origin directories
    train_files = 'dataset/Emergency_Vehicles/train'
    val_files = 'dataset/Emergency_Vehicles/test'
    
    # CSV files
    train_csv = 'dataset/Emergency_Vehicles/train.csv'
    val_csv = 'dataset/Emergency_Vehicles/sample_submission.csv'
    
    # New directories with organized files
    new_train_emergency_dir = 'data/train/emergency'
    new_train_non_emergency_dir = 'data/train/non-emergency'
    
    new_val_emergency_dir = 'data/val/emergency'
    new_val_non_emergency_dir = 'data/val/non-emergency'
    
    # Create new directories for images
    os.makedirs(new_train_emergency_dir, exist_ok=True)
    os.makedirs(new_train_non_emergency_dir, exist_ok=True)
    os.makedirs(new_val_emergency_dir, exist_ok=True)
    os.makedirs(new_val_non_emergency_dir, exist_ok=True)    
    
    # reading CSV files
    train_labels = pd.read_csv(train_csv)
    val_labels = pd.read_csv(val_csv)
    
    # Will be used during selecting 20% rows for validation dataset
    num_rows = int(0.2 * len(train_labels))
    
    # Copy Train images (80% of origin train dataset)
    for index, row in train_labels.iloc[num_rows:].iterrows():
        file_name = row['image_names']
        class_label = row['emergency_or_not']
        
        source_path = os.path.join(train_files, file_name)
        
        if class_label == 0:
            destination_path = os.path.join(new_train_non_emergency_dir, file_name)
        elif class_label == 1:
            destination_path = os.path.join(new_train_emergency_dir, file_name)
            
        if os.path.isfile(source_path):
            shutil.copy(source_path, destination_path)
            print(f"Copied {file_name} to {destination_path}")
        else:
            print(f"File {file_name} not found in {source_path}")
            
    # Select Val images (20% of train images)
    for index, row in train_labels.iloc[:num_rows].iterrows():
        file_name = row['image_names']
        class_label = row['emergency_or_not']
        
        source_path = os.path.join(train_files, file_name)
        
        if class_label == 0:
            destination_path = os.path.join(new_val_non_emergency_dir, file_name)
        elif class_label == 1:
            destination_path = os.path.join(new_val_emergency_dir, file_name)
            
        if os.path.isfile(source_path):
            shutil.copy(source_path, destination_path)
            print(f"Copied {file_name} to {destination_path}")
        else:
            print(f"File {file_name} not found in {source_path}")
            
            
if __name__ == "__main__":
    organize_files()