import { Injectable } from '@nestjs/common';

@Injectable()
export class AppService {
  getHello() {
    return {
      language: 'javascript',
      message: `Hello World from ${process.env.NAME_SERVICE}`,
    };
  }
}
