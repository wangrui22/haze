#ifndef MED_IMAGING_GL_ENVIRONMENT_H_
#define MED_IMAGING_GL_ENVIRONMENT_H_





class  GLEnvironment
{
public:
    GLEnvironment();

    ~GLEnvironment();

    //OpenGL �汾��Ϣ
    void get_gl_version(int &major , int &minor);

    //OpenGL ��ʵ�ֳ���
    std::string get_gl_vendor();

    //OpenGL ��Ⱦ����Ӳ��ƽ̨��
    std::string get_gl_renderer();

protected:

private:
};



#endif