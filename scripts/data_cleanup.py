# Advanced Data Cleanup Script

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def clean_data(file_path):
    """
    Clean up the data in the CSV file.
    
    Args:
    - file_path (str): The path to the CSV file.
    
    Returns:
    - cleaned_data (DataFrame): The cleaned DataFrame.
    """
    # Read the CSV file
    data = pd.read_csv(file_path)
    
    # Perform data cleaning operations
    
    # Handle missing values using mean imputation for numerical columns
    numerical_columns = data.select_dtypes(include=np.number).columns
    imputer = SimpleImputer(strategy='mean')
    data[numerical_columns] = imputer.fit_transform(data[numerical_columns])
    
    # Handle categorical variables using mode imputation
    categorical_columns = data.select_dtypes(exclude=np.number).columns
    for col in categorical_columns:
        data[col].fillna(data[col].mode()[0], inplace=True)
    
    # Remove duplicates
    data.drop_duplicates(inplace=True)
    
    # Perform additional cleaning if needed
    
    return data

def preprocess_data(cleaned_data):
    """
    Preprocess the cleaned data.
    
    Args:
    - cleaned_data (DataFrame): The cleaned DataFrame.
    
    Returns:
    - preprocessed_data (DataFrame): The preprocessed DataFrame.
    """
    # Feature scaling using StandardScaler
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(cleaned_data)
    
    # Dimensionality reduction using Principal Component Analysis (PCA)
    pca = PCA(n_components=0.95)  # Retain 95% of variance
    preprocessed_data = pca.fit_transform(scaled_data)
    
    return preprocessed_data

def save_preprocessed_data(preprocessed_data, output_path):
    """
    Save the preprocessed data to a new CSV file.
    
    Args:
    - preprocessed_data (DataFrame): The preprocessed DataFrame.
    - output_path (str): The path to save the preprocessed CSV file.
    """
    # Convert preprocessed data to DataFrame
    preprocessed_df = pd.DataFrame(preprocessed_data)
    
    # Save the preprocessed data to a new CSV file
    preprocessed_df.to_csv(output_path, index=False)
    print("Preprocessed data saved to:", output_path)

# Example usage
if __name__ == "__main__":
    input_file = "data/raw_data.csv"
    output_file = "data/preprocessed_data.csv"
    
    # Clean the data
    cleaned_data = clean_data(input_file)
    
    # Preprocess the cleaned data
    preprocessed_data = preprocess_data(cleaned_data)
    
    # Save the preprocessed data
    save_preprocessed_data(preprocessed_data, output_file)
