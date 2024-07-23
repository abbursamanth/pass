import time
import itertools
import string
import streamlit as st
from itertools import permutations, product

# Password cracking functions
def brute_force(password):
    start_time = time.time()
    characters = string.ascii_letters + string.digits + string.punctuation
    for length in range(1, len(password) + 1):
        for guess in itertools.product(characters, repeat=length):
            guess = ''.join(guess)
            print(f"Brute Force trying: {guess}")
            if guess == password:
                end_time = time.time()
                return guess, end_time - start_time

def brute_force_time_complexity(password_length):
    return "O(c^n)"  # where c is the number of possible characters, and n is the password length

def backtracking(password, guess='', characters=string.ascii_letters + string.digits + string.punctuation):
    print(f"Backtracking trying: {guess}")
    if len(guess) == len(password):
        if guess == password:
            return guess
        return None
    
    for char in characters:
        result = backtracking(password, guess + char)
        if result:
            return result

def backtracking_password(password):
    start_time = time.time()
    result = backtracking(password)
    end_time = time.time()
    return result, end_time - start_time

def backtracking_time_complexity(password_length):
    return "O(n * c^n)"  # where n is the password length and c is the number of possible characters

# Permutation and combination functions
def permute(s):
    perm = permutations(s)
    return [''.join(p) for p in perm]

def permute_with_repetition(s):
    prod = product(s, repeat=len(s))
    return [''.join(p) for p in prod]

# Streamlit interface
st.title('Tool for Password Cracking, Permutations, and Combinations')

password = st.text_input('Enter the password to crack or string to permute/combine:', type='password')

col1, col2, col3 = st.columns(3)

with col1:
    if st.button('Get Combinations'):
        if password:
            combinations = permute_with_repetition(password)
            st.subheader('Combinations with Repetition')
            st.write(combinations)
        else:
            st.warning('Please enter a string for combinations.')

with col2:
    if st.button('Get Permutations'):
        if password:
            permutations_result = permute(password)
            st.subheader('Permutations')
            st.write(permutations_result)
        else:
            st.warning('Please enter a string for permutations.')

with col3:
    if st.button('Crack Password'):
        if password:
            brute_force_result, brute_force_time = brute_force(password)
            backtracking_result, backtracking_time = backtracking_password(password)

            st.subheader('Results')
            st.write(f"Password: {password}")

            st.write("### Brute Force")
            st.write(f"Cracked Password: {brute_force_result}")
            st.write(f"Time Taken: {brute_force_time:.4f} seconds")
            st.write(f"Time Complexity: {brute_force_time_complexity(len(password))}")

            st.write("### Backtracking")
            st.write(f"Cracked Password: {backtracking_result}")
            st.write(f"Time Taken: {backtracking_time:.4f} seconds")
            st.write(f"Time Complexity: {backtracking_time_complexity(len(password))}")

            st.write("### Most Efficient Algorithm")
            if brute_force_time < backtracking_time:
                st.write("Brute Force is more efficient.")
            else:
                st.write("Backtracking is more efficient.")
        else:
            st.warning('Please enter a password to crack.')
