FROM centos/python-36-centos7
USER root
RUN mkdir /app
COPY . /app
COPY node.kubeconfig /app/sgrudah/
COPY node.kubeconfig .
RUN pip install -r /app/requirements.txt
EXPOSE 80
ENTRYPOINT ["python"]
CMD ["/app/sgrudah/sgrudah.py"]
