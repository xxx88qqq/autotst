#ifndef SUBWIDGET_H
#define SUBWIDGET_H

#include <QWidget>
#include <QButtonGroup>


namespace Ui {
class subwidget;
}

class subwidget : public QWidget
{
    Q_OBJECT

public:
    explicit subwidget(QWidget *parent = nullptr);
    ~subwidget();

private slots:
    void on_buttonBox_clicked(QAbstractButton *button);

private:
    Ui::subwidget *ui;
};

#endif // SUBWIDGET_H
