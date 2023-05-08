{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "91529dc7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pillow in e:\\anaconda\\lib\\site-packages (9.4.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install pillow"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e42e9008",
   "metadata": {},
   "outputs": [],
   "source": [
    "import tkinter as tk"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "fd5a90a5",
   "metadata": {},
   "outputs": [],
   "source": [
    "from PIL import Image, ImageTk"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "5cf85818",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Zhixuan Zhang\\AppData\\Local\\Temp\\ipykernel_13016\\3001569461.py:13: DeprecationWarning: ANTIALIAS is deprecated and will be removed in Pillow 10 (2023-07-01). Use LANCZOS or Resampling.LANCZOS instead.\n",
      "  image = image.resize((width, height), Image.ANTIALIAS)\n"
     ]
    },
    {
     "ename": "TclError",
     "evalue": "image \"pyimage17\" doesn't exist",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTclError\u001b[0m                                  Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[17], line 17\u001b[0m\n\u001b[0;32m     14\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m ImageTk\u001b[38;5;241m.\u001b[39mPhotoImage(image)\n\u001b[0;32m     16\u001b[0m image \u001b[38;5;241m=\u001b[39m load_resized_image(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124massistant_image.png\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;241m200\u001b[39m, \u001b[38;5;241m200\u001b[39m)\n\u001b[1;32m---> 17\u001b[0m image_label \u001b[38;5;241m=\u001b[39m \u001b[43mtk\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mLabel\u001b[49m\u001b[43m(\u001b[49m\u001b[43mwindow\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mimage\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mimage\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m     18\u001b[0m image_label\u001b[38;5;241m.\u001b[39mpack()\n\u001b[0;32m     20\u001b[0m window\u001b[38;5;241m.\u001b[39mmainloop()\n",
      "File \u001b[1;32mE:\\anaconda\\lib\\tkinter\\__init__.py:3148\u001b[0m, in \u001b[0;36mLabel.__init__\u001b[1;34m(self, master, cnf, **kw)\u001b[0m\n\u001b[0;32m   3130\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21m__init__\u001b[39m(\u001b[38;5;28mself\u001b[39m, master\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mNone\u001b[39;00m, cnf\u001b[38;5;241m=\u001b[39m{}, \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mkw):\n\u001b[0;32m   3131\u001b[0m     \u001b[38;5;124;03m\"\"\"Construct a label widget with the parent MASTER.\u001b[39;00m\n\u001b[0;32m   3132\u001b[0m \n\u001b[0;32m   3133\u001b[0m \u001b[38;5;124;03m    STANDARD OPTIONS\u001b[39;00m\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m   3146\u001b[0m \n\u001b[0;32m   3147\u001b[0m \u001b[38;5;124;03m    \"\"\"\u001b[39;00m\n\u001b[1;32m-> 3148\u001b[0m     \u001b[43mWidget\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[38;5;21;43m__init__\u001b[39;49m\u001b[43m(\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mmaster\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mlabel\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mcnf\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mkw\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32mE:\\anaconda\\lib\\tkinter\\__init__.py:2572\u001b[0m, in \u001b[0;36mBaseWidget.__init__\u001b[1;34m(self, master, widgetName, cnf, kw, extra)\u001b[0m\n\u001b[0;32m   2570\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m k, v \u001b[38;5;129;01min\u001b[39;00m classes:\n\u001b[0;32m   2571\u001b[0m     \u001b[38;5;28;01mdel\u001b[39;00m cnf[k]\n\u001b[1;32m-> 2572\u001b[0m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mtk\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mcall\u001b[49m\u001b[43m(\u001b[49m\n\u001b[0;32m   2573\u001b[0m \u001b[43m    \u001b[49m\u001b[43m(\u001b[49m\u001b[43mwidgetName\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_w\u001b[49m\u001b[43m)\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m+\u001b[39;49m\u001b[43m \u001b[49m\u001b[43mextra\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m+\u001b[39;49m\u001b[43m \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_options\u001b[49m\u001b[43m(\u001b[49m\u001b[43mcnf\u001b[49m\u001b[43m)\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m   2574\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m k, v \u001b[38;5;129;01min\u001b[39;00m classes:\n\u001b[0;32m   2575\u001b[0m     k\u001b[38;5;241m.\u001b[39mconfigure(\u001b[38;5;28mself\u001b[39m, v)\n",
      "\u001b[1;31mTclError\u001b[0m: image \"pyimage17\" doesn't exist"
     ]
    }
   ],
   "source": [
    "import datetime\n",
    "import os\n",
    "import tkinter as tk\n",
    "from PIL import Image, ImageTk\n",
    "\n",
    "# 创建一个窗口\n",
    "window = tk.Tk()\n",
    "window.title(\"桌面管理助手\")\n",
    "\n",
    "# 添加助手图片\n",
    "def load_resized_image(path, width, height):\n",
    "    image = Image.open(path)\n",
    "    image = image.resize((width, height), Image.ANTIALIAS)\n",
    "    return ImageTk.PhotoImage(image)\n",
    "\n",
    "image = load_resized_image('assistant_image.png', 200, 200)\n",
    "image_label = tk.Label(window, image=image)\n",
    "image_label.pack()\n",
    "\n",
    "window.mainloop()\n",
    "'''\n",
    "# 添加功能按钮和标签\n",
    "frame = tk.Frame(window)\n",
    "frame.pack(side=tk.RIGHT)\n",
    "\n",
    "# 显示系统实时时间\n",
    "def show_time():\n",
    "    current_time = datetime.datetime.now().strftime(\"%Y-%m-%d %H:%M:%S\")\n",
    "    time_label.config(text=current_time)\n",
    "    window.after(1000, show_time)  # 每1000毫秒（1秒）更新一次时间\n",
    "\n",
    "time_label = tk.Label(frame, text=\"时间\")\n",
    "time_label.pack()\n",
    "show_time()\n",
    "time_button = tk.Button(frame, text=\"显示时间\", command=show_time)\n",
    "time_button.pack()\n",
    "\n",
    "# 文件名，用于保存签到数据\n",
    "SIGN_IN_FILE = \"sign_in_data.txt\"\n",
    "\n",
    "# 检查今天是否已签到\n",
    "def check_today_signed_in():\n",
    "    today = datetime.date.today().strftime(\"%Y-%m-%d\")\n",
    "\n",
    "    if os.path.exists(SIGN_IN_FILE):\n",
    "        with open(SIGN_IN_FILE, \"r\") as f:\n",
    "            dates = f.readlines()\n",
    "            for date in dates:\n",
    "                if date.strip() == today:\n",
    "                    return True\n",
    "    return False\n",
    "\n",
    "FAVORABILITY_FILE = \"favorability.txt\"\n",
    "\n",
    "# 读取好感度值\n",
    "def read_favorability():\n",
    "    if os.path.exists(FAVORABILITY_FILE):\n",
    "        with open(FAVORABILITY_FILE, \"r\") as f:\n",
    "            favorability = int(f.read())\n",
    "    else:\n",
    "        favorability = 0\n",
    "    return favorability\n",
    "\n",
    "# 保存好感度值\n",
    "def save_favorability(favorability):\n",
    "    with open(FAVORABILITY_FILE, \"w\") as f:\n",
    "        f.write(str(favorability))\n",
    "\n",
    "# 计算等级\n",
    "def calculate_level(favorability):\n",
    "    return favorability // 100 + 1\n",
    "\n",
    "# 显示好感度等级系统\n",
    "def show_favorability():\n",
    "    favorability = read_favorability()\n",
    "    level = calculate_level(favorability)\n",
    "    favorability_label.config(text=f\"好感度: {favorability} 等级: {level}\")\n",
    "\n",
    "# 签到功能（更新好感度）\n",
    "def sign_in():\n",
    "    favorability = read_favorability()\n",
    "    favorability += 10\n",
    "    save_favorability(favorability)\n",
    "    today = datetime.date.today().strftime(\"%Y-%m-%d\")\n",
    "    \n",
    "    with open(SIGN_IN_FILE, \"a\") as f:\n",
    "        f.write(today + \"\\n\")\n",
    "    \n",
    "    sign_in_button.config(state=\"disabled\", text=\"已签到\")\n",
    "    show_favorability()\n",
    "\n",
    "# 在GUI中创建好感度标签和签到按钮\n",
    "favorability_label = tk.Label(frame)\n",
    "favorability_label.pack()\n",
    "\n",
    "sign_in_button = tk.Button(frame, text=\"签到\", command=sign_in)\n",
    "sign_in_button.pack()\n",
    "\n",
    "# 显示初始好感度和等级\n",
    "show_favorability()\n",
    "\n",
    "# 如果今天已签到，禁用签到按钮\n",
    "if check_today_signed_in():\n",
    "    sign_in_button.config(state=\"disabled\", text=\"已签到\")\n",
    "\n",
    "\n",
    "# 运行窗口\n",
    "window.mainloop()\n",
    "\n",
    "\n",
    "\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fc9a6a47",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a9554395",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.16"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
