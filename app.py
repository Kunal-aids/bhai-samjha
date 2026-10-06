import streamlit as st

st.title("BhaiSamjha - Python Error in Hinglish")
st.write("BCA Freshers ke liye, English error ka Hinglish matlab")

error_dict = {
    "IndentationError": "Bhai space ka issue hai. Python me aage-peeche ka space matter karta hai. Tab ya 4 space ka dhyan de.",
    "SyntaxError": "Bhai likhne me galti hai. Kahin bracket, colon (:) ya quote miss ho gaya hai.",
    "NameError": "Bhai naam galat likh diya. Variable banaya hi nahi aur use karne laga.",
    "TypeError": "Bhai type ka locha hai. Tu number aur string ko ek saath jod raha hai.",
    "ZeroDivisionError": "Bhai 0 se divide kar diya. Maths me bhi ye allowed nahi hai.",
    "ValueError": "Bhai value galat daal di. int() me tu string daal raha hai.",
    "IndexError": "Bhai list se bahar ja raha hai. List me 3 item hai aur tu 5th mang raha hai.",
    "KeyError": "Bhai dictionary me ye key hai hi nahi. Spelling check kar.",
    "AttributeError": "Bhai is cheez me ye feature hai hi nahi. .append() list pe lagta hai, string pe nahi.",
    "ImportError": "Bhai library install nahi hai ya naam galat likha hai. pip install karna padega.",
    "ModuleNotFoundError": "Bhai module mila hi nahi. Naam check kar ya install kar.",
    "FileNotFoundError": "Bhai file ka naam ya path galat hai. File us folder me hai hi nahi.",
    "UnboundLocalError": "Bhai function ke andar variable pehle use kar liya, banaya baad me hai.",
    "TabError": "Bhai kahin Tab aur kahin Space use kar diya. Ek hi use kar.",
    "OverflowError": "Bhai number bahut bada ho gaya, computer handle nahi kar paya.",
    "RecursionError": "Bhai function khud ko baar-baar call kar raha hai, loop me fas gaya.",
    "MemoryError": "Bhai RAM full ho gayi. List bahut badi bana di tune.",
    "PermissionError": "Bhai file ko permission nahi hai. File open hai ya admin rights chahiye.",
    "IsADirectoryError": "Bhai tu folder ko file samajh ke khol raha hai.",
    "NotADirectoryError": "Bhai tu file ko folder samajh raha hai.",
    "StopIteration": "Bhai loop khatam ho gaya, ab aur item nahi hai.",
    "AssertionError": "Bhai tera assert condition fail ho gaya. Check kar condition.",
    "EOFError": "Bhai input khatam ho gaya, user ne kuch diya hi nahi.",
    "FloatingPointError": "Bhai decimal wale number me calculation fail ho gayi.",
    "KeyboardInterrupt": "Bhai tune Ctrl+C dabake program rok diya.",
    "SystemError": "Bhai Python ka internal issue hai, tera code nahi.",
    "OSError": "Bhai system ka error hai, file ya OS se related.",
    "ConnectionError": "Bhai internet ya connection ka issue hai.",
    "TimeoutError": "Bhai time khatam ho gaya, system ne wait karna band kar diya."
}

user_error = st.text_input("Apna Python Error yaha paste kar:")

if user_error:
    found = False
    for key, value in error_dict.items():
        if key.lower() in user_error.lower():
            st.success(f"**{key}**")
            st.info(f"**Matlab:** {value}")
            found = True
            break
    if not found:
        st.warning("Bhai ye error naya lag raha hai, main isko jaldi add kar dunga!")