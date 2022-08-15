{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "be692ff9",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, render_template, request\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "234f6450",
   "metadata": {},
   "outputs": [],
   "source": [
    "app=Flask(__name__)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "a2ffe868",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/\",methods=[\"GET\",\"POST\"])\n",
    "def indes():\n",
    "    if request.method == \"POST\":\n",
    "        rates = float(request.form.get(\"rates\"))\n",
    "        print(rates)\n",
    "        model1 = joblib.load(\"regression_DBS\")\n",
    "        r1 = model1.predict([[rates]])\n",
    "        model2 = joblib.load(\"tree_DBS\")\n",
    "        r2 = model2.predict([[rates]])   \n",
    "        return (render_template(\"index.html\",result1=\"temp\",result2=\"temp\"))\n",
    "    else:\n",
    "        return (render_template(\"index.html\",result1=\"waiting\",result2=\"waiting\"))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "1f341c9e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "ename": "OSError",
     "evalue": "[Errno 48] Address already in use",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mOSError\u001b[0m                                   Traceback (most recent call last)",
      "Input \u001b[0;32mIn [6]\u001b[0m, in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;18m__name__\u001b[39m\u001b[38;5;241m==\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m__main__\u001b[39m\u001b[38;5;124m\"\u001b[39m:\n\u001b[0;32m----> 2\u001b[0m     \u001b[43mapp\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mrun\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[0;32m~/opt/anaconda3/lib/python3.9/site-packages/flask/app.py:990\u001b[0m, in \u001b[0;36mFlask.run\u001b[0;34m(self, host, port, debug, load_dotenv, **options)\u001b[0m\n\u001b[1;32m    987\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mwerkzeug\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mserving\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m run_simple\n\u001b[1;32m    989\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[0;32m--> 990\u001b[0m     \u001b[43mrun_simple\u001b[49m\u001b[43m(\u001b[49m\u001b[43mhost\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mport\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43moptions\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    991\u001b[0m \u001b[38;5;28;01mfinally\u001b[39;00m:\n\u001b[1;32m    992\u001b[0m     \u001b[38;5;66;03m# reset the first request information if the development server\u001b[39;00m\n\u001b[1;32m    993\u001b[0m     \u001b[38;5;66;03m# reset normally.  This makes it possible to restart the server\u001b[39;00m\n\u001b[1;32m    994\u001b[0m     \u001b[38;5;66;03m# without reloader and that stuff from an interactive shell.\u001b[39;00m\n\u001b[1;32m    995\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_got_first_request \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mFalse\u001b[39;00m\n",
      "File \u001b[0;32m~/opt/anaconda3/lib/python3.9/site-packages/werkzeug/serving.py:1017\u001b[0m, in \u001b[0;36mrun_simple\u001b[0;34m(hostname, port, application, use_reloader, use_debugger, use_evalex, extra_files, exclude_patterns, reloader_interval, reloader_type, threaded, processes, request_handler, static_files, passthrough_errors, ssl_context)\u001b[0m\n\u001b[1;32m   1009\u001b[0m     _rwr(\n\u001b[1;32m   1010\u001b[0m         inner,\n\u001b[1;32m   1011\u001b[0m         extra_files\u001b[38;5;241m=\u001b[39mextra_files,\n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m   1014\u001b[0m         reloader_type\u001b[38;5;241m=\u001b[39mreloader_type,\n\u001b[1;32m   1015\u001b[0m     )\n\u001b[1;32m   1016\u001b[0m \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[0;32m-> 1017\u001b[0m     \u001b[43minner\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[0;32m~/opt/anaconda3/lib/python3.9/site-packages/werkzeug/serving.py:957\u001b[0m, in \u001b[0;36mrun_simple.<locals>.inner\u001b[0;34m()\u001b[0m\n\u001b[1;32m    955\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m (\u001b[38;5;167;01mLookupError\u001b[39;00m, \u001b[38;5;167;01mValueError\u001b[39;00m):\n\u001b[1;32m    956\u001b[0m     fd \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[0;32m--> 957\u001b[0m srv \u001b[38;5;241m=\u001b[39m \u001b[43mmake_server\u001b[49m\u001b[43m(\u001b[49m\n\u001b[1;32m    958\u001b[0m \u001b[43m    \u001b[49m\u001b[43mhostname\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    959\u001b[0m \u001b[43m    \u001b[49m\u001b[43mport\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    960\u001b[0m \u001b[43m    \u001b[49m\u001b[43mapplication\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    961\u001b[0m \u001b[43m    \u001b[49m\u001b[43mthreaded\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    962\u001b[0m \u001b[43m    \u001b[49m\u001b[43mprocesses\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    963\u001b[0m \u001b[43m    \u001b[49m\u001b[43mrequest_handler\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    964\u001b[0m \u001b[43m    \u001b[49m\u001b[43mpassthrough_errors\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    965\u001b[0m \u001b[43m    \u001b[49m\u001b[43mssl_context\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    966\u001b[0m \u001b[43m    \u001b[49m\u001b[43mfd\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mfd\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    967\u001b[0m \u001b[43m\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    968\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m fd \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[1;32m    969\u001b[0m     log_startup(srv\u001b[38;5;241m.\u001b[39msocket)\n",
      "File \u001b[0;32m~/opt/anaconda3/lib/python3.9/site-packages/werkzeug/serving.py:789\u001b[0m, in \u001b[0;36mmake_server\u001b[0;34m(host, port, app, threaded, processes, request_handler, passthrough_errors, ssl_context, fd)\u001b[0m\n\u001b[1;32m    787\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcannot have a multithreaded and multi process server.\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m    788\u001b[0m \u001b[38;5;28;01melif\u001b[39;00m threaded:\n\u001b[0;32m--> 789\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mThreadedWSGIServer\u001b[49m\u001b[43m(\u001b[49m\n\u001b[1;32m    790\u001b[0m \u001b[43m        \u001b[49m\u001b[43mhost\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mport\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mapp\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mrequest_handler\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mpassthrough_errors\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mssl_context\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mfd\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mfd\u001b[49m\n\u001b[1;32m    791\u001b[0m \u001b[43m    \u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    792\u001b[0m \u001b[38;5;28;01melif\u001b[39;00m processes \u001b[38;5;241m>\u001b[39m \u001b[38;5;241m1\u001b[39m:\n\u001b[1;32m    793\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m ForkingWSGIServer(\n\u001b[1;32m    794\u001b[0m         host,\n\u001b[1;32m    795\u001b[0m         port,\n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m    801\u001b[0m         fd\u001b[38;5;241m=\u001b[39mfd,\n\u001b[1;32m    802\u001b[0m     )\n",
      "File \u001b[0;32m~/opt/anaconda3/lib/python3.9/site-packages/werkzeug/serving.py:693\u001b[0m, in \u001b[0;36mBaseWSGIServer.__init__\u001b[0;34m(self, host, port, app, handler, passthrough_errors, ssl_context, fd)\u001b[0m\n\u001b[1;32m    690\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m os\u001b[38;5;241m.\u001b[39mpath\u001b[38;5;241m.\u001b[39mexists(server_address):\n\u001b[1;32m    691\u001b[0m         os\u001b[38;5;241m.\u001b[39munlink(server_address)\n\u001b[0;32m--> 693\u001b[0m \u001b[38;5;28;43msuper\u001b[39;49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[38;5;21;43m__init__\u001b[39;49m\u001b[43m(\u001b[49m\u001b[43mserver_address\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mhandler\u001b[49m\u001b[43m)\u001b[49m  \u001b[38;5;66;03m# type: ignore\u001b[39;00m\n\u001b[1;32m    695\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mapp \u001b[38;5;241m=\u001b[39m app\n\u001b[1;32m    696\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mpassthrough_errors \u001b[38;5;241m=\u001b[39m passthrough_errors\n",
      "File \u001b[0;32m~/opt/anaconda3/lib/python3.9/socketserver.py:452\u001b[0m, in \u001b[0;36mTCPServer.__init__\u001b[0;34m(self, server_address, RequestHandlerClass, bind_and_activate)\u001b[0m\n\u001b[1;32m    450\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m bind_and_activate:\n\u001b[1;32m    451\u001b[0m     \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[0;32m--> 452\u001b[0m         \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mserver_bind\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    453\u001b[0m         \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mserver_activate()\n\u001b[1;32m    454\u001b[0m     \u001b[38;5;28;01mexcept\u001b[39;00m:\n",
      "File \u001b[0;32m~/opt/anaconda3/lib/python3.9/http/server.py:136\u001b[0m, in \u001b[0;36mHTTPServer.server_bind\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    134\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mserver_bind\u001b[39m(\u001b[38;5;28mself\u001b[39m):\n\u001b[1;32m    135\u001b[0m     \u001b[38;5;124;03m\"\"\"Override server_bind to store the server name.\"\"\"\u001b[39;00m\n\u001b[0;32m--> 136\u001b[0m     \u001b[43msocketserver\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mTCPServer\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mserver_bind\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m)\u001b[49m\n\u001b[1;32m    137\u001b[0m     host, port \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mserver_address[:\u001b[38;5;241m2\u001b[39m]\n\u001b[1;32m    138\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mserver_name \u001b[38;5;241m=\u001b[39m socket\u001b[38;5;241m.\u001b[39mgetfqdn(host)\n",
      "File \u001b[0;32m~/opt/anaconda3/lib/python3.9/socketserver.py:466\u001b[0m, in \u001b[0;36mTCPServer.server_bind\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    464\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mallow_reuse_address:\n\u001b[1;32m    465\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39msocket\u001b[38;5;241m.\u001b[39msetsockopt(socket\u001b[38;5;241m.\u001b[39mSOL_SOCKET, socket\u001b[38;5;241m.\u001b[39mSO_REUSEADDR, \u001b[38;5;241m1\u001b[39m)\n\u001b[0;32m--> 466\u001b[0m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43msocket\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mbind\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mserver_address\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    467\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mserver_address \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39msocket\u001b[38;5;241m.\u001b[39mgetsockname()\n",
      "\u001b[0;31mOSError\u001b[0m: [Errno 48] Address already in use"
     ]
    }
   ],
   "source": [
    "if __name__== \"__main__\":\n",
    "    app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9a773fe2",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f16b6a99",
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
